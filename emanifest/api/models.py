from django.core.validators import RegexValidator
from django.db import models


# TODO for int'l
# Update phone to 20
# Update state to "state/providence/region"


class Address(models.Model):

    COUNTRIES = (
        ('US', 'United States'),
        ('MX', 'Mexico'),
        ('PR', 'Puerto Rico'),
    )

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


class DesinatedFacility(models.Model):
    name = models.CharField(max_length=200)
    address = models.ForeignKey('Address')
    epa_id = models.CharField(max_length=200)
    phone = models.CharField(max_length=12)

    def as_json(self):
        address = self.address.as_json()

        return dict(
            name=self.name,
            phone=self.phone,
            address=address,
            epa_id=self.epa_id,
        )


# The way that addresses are handled here should be thought out better.
# This is a quick hack for demo purposes.
class Generator(models.Model):
    name = models.CharField(max_length=40)
    phone = models.CharField(max_length=12)
    address = models.ForeignKey('Address')
    mailing_address = models.ForeignKey('Address',
                                        related_name='mailing_address',
                                        null=True, blank=True)
    mailing_and_address_same = models.BooleanField()

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
    phone_help = "Phone number 9-15 digits, entered in the format: '999999999'"
    phone_regex = RegexValidator(regex=r'^\d{9,15}$', message=phone_help)
    emergency_phone = models.CharField(validators=[phone_regex], max_length=15)

    international = models.ForeignKey('International', null=True, blank=True)
    designated_facility = models.ForeignKey('DesinatedFacility')

    special_instructions = models.TextField(blank=True)

    # This is included, b/c maybe it could be used as a way to validate
    number_of_pages = models.IntegerField()  # 2

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
        transporters = [t.as_json() for t in transporters]

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


class Transporter(models.Model):
    manifest = models.ForeignKey('Manifest')  # 6, 7
    name = models.CharField(max_length=200)
    epa_id = models.CharField(max_length=12)
    # aknowledgement_name = models.CharField(max_length=200)
    # aknowledgement = ?? signature
    # aknowledgement_date = models.DateField()

    def __str__(self):
        return self.name, self.epa_id

    def as_json(self):

        return dict(
            name=self.name,
            epa_id=self.epa_id,
        )


class WasteCode(models.Model):
    WASTE_CODE_TYPES = (
        ('Federal', 'Federal'),
        ('State', 'State'),
    )

    code = models.CharField(max_length=10, null=True, blank=True)
    code_type = models.CharField(max_length=10, choices=WASTE_CODE_TYPES)

    def as_json(self):

        return dict(
            code=self.code,
            code_type=self.code_type,
        )


class ManifestedWaste(models.Model):

    manifest = models.ForeignKey('Manifest')

    hazardous_waste = models.BooleanField()  # 9a HM
    description = models.TextField(null=True, blank=True)

    # (including Proper Shipping Name, Hazard Class, ID Number, and
    # Packing Group (if any))

    container_quantity = models.IntegerField()
    container_type = models.CharField(max_length=5)

    total_quantity = models.IntegerField()      # total quantity # 11
    units_of_measure = models.CharField(max_length=5)  # 12
    waste_codes = models.ForeignKey('WasteCode', null=True, blank=True)  # 13

    def as_json(self):
        waste_codes = self.waste_codes.as_json()

        return dict(
            hazardous_waste=self.hazardous_waste,
            description=self.description,
            container_quantity=self.container_quantity,
            container_type=self.container_type,
            total_quantity=self.total_quantity,
            units_of_measure=self.units_of_measure,
            waste_codes=waste_codes,
        )
