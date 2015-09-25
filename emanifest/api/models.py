from django.db import models

from api.common import (
    CONTAINER_TYPES,
    COUNTRIES,
    DOT_GROUPS,
    UNITS_OF_MEASURE,
    WASTE_CODE_TYPES
)

# TODO for int'l
# Update phone to 20
# Update state to "state/providence/region"
# TODO: Validate address & phone for designated facility


class EPAEntity(models.Model):

    name = models.CharField(max_length=40)
    # TODO: EPA ID: XXX123456789 -- if we are validating on this.
    epa_id = models.CharField(max_length=12)

    def __str__(self):
        return ', '.join([self.name, self.epa_id])

    def as_json(self):
        return dict(
            name=self.name,
            epa_id=self.epa_id,
        )


class Address(models.Model):

    address_line_1 = models.CharField(max_length=60)
    address_line_2 = models.CharField(max_length=60, blank=True, null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)  # "state/providence/region"
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100, choices=COUNTRIES, default='US')

    def __str__(self):
        state_line = self.city + ', ' + self.state + ' ' + self.postal_code
        address = (
            self.address_line_1,
            self.address_line_2,
            state_line,
            self.country
        )
        return ', '.join(address)

    def as_json(self):

        return dict(
            address_line_1=self.address_line_1,
            address_line_2=self.address_line_2,
            city=self.city,
            state=self.state,
            postal_code=self.postal_code,
            country=self.country,
        )


class Signature(models.Model):
    """
    sig_statement_default = "I hereby declare that the contents \
        of this consignment are fully and \
        accurately described above by the proper shipping name, and are \
        classified, packaged, marked and labeled/placarded, and are in all \
        respects in proper condition for transport according to applicable \
        international and national governmental regulations. If export \
        shipment and I am the Primary Exporter, I certify that the \
        contents of this consignment conform to the terms of the \
        attached EPA Acknowledgment of Consent. I certify that the waste \
        minimization statement identified in 40 CFR 262.27(a) (if I am a \
        large quantity generator) or (b) (if I am a small quantity \
        generator) is true."
    """

    signature_name = models.CharField(max_length=200, null=True, blank=True)
    # certification_statments = models.TextField(default=sig_statement_default,
    #                                           null=True, blank=True)
    signature_date = models.DateField(null=True, blank=True)
    # signature = models.CharField(max_length=200, null=True, blank=True)

    # aknowledgement_name = models.CharField(max_length=200)
    # aknowledgement = ?? signature
    # aknowledgement_date = models.DateField()


# The way that addresses are handled here should be thought out better.
# This is a quick hack for demo purposes.
class Generator(EPAEntity):

    phone = models.CharField(max_length=12)
    site_address = models.ForeignKey('Address', related_name='site_address')
    mailing_address = models.ForeignKey('Address',
                                        related_name='mailing_address',
                                        null=True, blank=True)
    mailing_and_address_same = models.BooleanField()

    signature = models.ForeignKey('signature')

    def as_json(self):
        address = self.address.as_json()
        mailing_address = self.mailing_address.as_json()

        return dict(
            name=self.name,
            phone=self.phone,
            address=address,
            mailing_and_address_are_the_same=self.mailing_and_address_same,
            mailing_address=mailing_address,
        )


class International(models.Model):  # 16
    import_to_us = models.BooleanField()
    export_from_us = models.BooleanField()
    port = models.CharField(max_length=200)
    date_at_port = models.DateField()
    # transporter_signature = ??

    def as_json(self):

        international_dict = dict(
            import_to_us=self.import_to_us,
            export_to_us=self.export_to_us,
            port=self.port,
            date_at_port=self.date_at_port,
        )

        print(type(international_dict))

        return international_dict


class DesignatedFacility(EPAEntity):
    address = models.ForeignKey('Address', null=True, blank=True)
    phone = models.CharField(max_length=12, null=True, blank=True)
    signature = models.ForeignKey('signature')


class Manifest(models.Model):
    # "ManifestTrackingNumber":"3 Letters  9 numbers",
    tracking_number = models.CharField(max_length=12)  # 4

    generator = models.ForeignKey('Generator')  # 1

    # TODO: How to validate -- emergency numbers internationally?
    # django local flavor -- validate the number by locality
    # "23 alphanumberic string accounting for international numbers
    # e.g. +001 1234321234, to be honest this is just a safety feature,
    # most will be standard 10 digit"
    # # 3
    # Removing these temporary
    # phone_help = "Phone number 9-15 digits, entered in the
    # format: '999999999' "
    # phone_regex = RegexValidator(regex=r'^\d{9,15}$', message=phone_help)
    emergency_phone = models.CharField(max_length=15)

    international = models.ForeignKey('International', null=True, blank=True)

    # 'DesinatedFacility'
    designated_facility = models.ForeignKey('DesignatedFacility')

    special_instructions = models.TextField(blank=True)
    # example:  Specific Gravity 1.2321, PO ID 102aif9i321
    # TODO: Compare these to sample data. Can we parse at this time?
    # special handling -- TextField
    # tracking instructions -- TextField
    # waste profile number -- 9 Charater pattern value=([0-9])+
    # container number -- 20 char
    # response guide number - 4 Alphanumeric pattern value=[0-9,a-z,A-Z](0-9)+

    # This is included, b/c maybe it could be used as a way to validate
    number_of_pages = models.IntegerField()  # 2

    discrepancy = models.BooleanField()
    # Should be validated against discrepancy -- if True, then desc req.
    discrepancy_description = models.TextField(blank=True, null=True)
    discrepancy_quantity = models.BooleanField(default=False)
    discrepancy_type = models.BooleanField(default=False)
    discrepancy_residue = models.BooleanField(default=False)
    partial_rejection = models.BooleanField(default=False)
    full_rejection = models.BooleanField(default=False)

    def __str__(self):
        return self.tracking_number

    def as_json(self):
        generator = self.generator.as_json()

        try:
            international = self.international.as_json()
        except AttributeError:
            international = {}

        designated_facility = self.designated_facility.as_json()

        transporters = Transporter.objects.filter(manifest_id=self.id)
        transporters = [t.transporter.as_json() for t in transporters]

        waste = ManifestedWaste.objects.filter(manifest_id=self.id)
        print(waste)
        waste = [w.as_json() for w in waste]

        return dict(
            tracking_number=self.tracking_number,
            generator=generator,
            emergency_phone=self.emergency_phone,
            international=international,
            designated_facility=designated_facility,
            special_instructions=self.special_instructions,
            number_of_pages=self.number_of_pages,
            transporters=transporters,
            waste=waste,
        )


class Transporter(EPAEntity):
    manifest = models.ForeignKey('Manifest')  # 6, 7
    signature = models.ForeignKey('signature')


class HazardousWasteReportCodes(models.Model):
    manifest = models.ForeignKey('Manifest')
    code = models.CharField(max_length=10)


class ManifestedWaste(models.Model):

    manifest = models.ForeignKey('Manifest')

    hazardous_waste = models.BooleanField()  # 9a HM
    # description = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    shipping_name = models.CharField(max_length=255, null=True, blank=True)
    hazard_class = models.CharField(max_length=300, null=True, blank=True)
    dot_id = models.CharField(max_length=6, null=True, blank=True)
    packing_group = models.CharField(max_length=6, choices=DOT_GROUPS,
                                     blank=True, default='')

    # (including Proper Shipping Name, Hazard Class, ID Number, and
    # Packing Group (if any))

    container_quantity = models.IntegerField()
    container_type = models.CharField(max_length=2, choices=CONTAINER_TYPES)

    total_quantity = models.IntegerField()      # total quantity # 11
    units_of_measure = models.CharField(max_length=1, choices=UNITS_OF_MEASURE)
    # 12

    def as_json(self):
        waste_codes = self.waste_codes.as_json()

        description = dict(
            description=self.dot_description,
            shipping_name=self.dot_shipping_name,
            hazard_class=self.dot_hazard_class,
            dot_id=self.dot_id,
            packing_group=self.dot_packing_group,
        )

        return dict(
            hazardous_waste=self.hazardous_waste,
            dot_description=description,
            container_quantity=self.container_quantity,
            container_type=self.container_type,
            total_quantity=self.total_quantity,
            units_of_measure=self.units_of_measure,
            waste_codes=waste_codes,
        )


class WasteCode(models.Model):
    waste_code = models.ForeignKey('ManifestedWaste')  # 13

    # if the code is federal then max length = 4
    # if the code it state, then max length = 8
    code = models.CharField(max_length=10)
    code_type = models.CharField(max_length=10, choices=WASTE_CODE_TYPES)

    def as_json(self):

        return dict(
            code=self.code,
            code_type=self.code_type,
        )
