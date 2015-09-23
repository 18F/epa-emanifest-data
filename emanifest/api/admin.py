from django.contrib import admin
from api.models import (
    Address, Transporter, EPAEntity,
    Generator, International, WasteCode,
    ManifestedWaste, Manifest
)


class ManifestInline(admin.TabularInline):
    model = Manifest


class TransporterInline(admin.TabularInline):
    model = Transporter


class ManifestedWasteInline(admin.TabularInline):
    model = ManifestedWaste


class GeneratorAdmin(admin.ModelAdmin):
    inlines = [
        ManifestInline,
    ]
    pass


class ManifestAdmin(admin.ModelAdmin):
    inlines = [
        TransporterInline, ManifestedWasteInline
    ]
    pass


class GenericAdmin(admin.ModelAdmin):
    pass

admin.site.register(Address, GenericAdmin)
admin.site.register(Transporter, GenericAdmin)
admin.site.register(EPAEntity, GenericAdmin)
admin.site.register(Generator, GeneratorAdmin)
admin.site.register(International, GenericAdmin)
admin.site.register(WasteCode, GenericAdmin)
admin.site.register(ManifestedWaste, GenericAdmin)
admin.site.register(Manifest, ManifestAdmin)
