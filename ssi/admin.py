from django.contrib import admin

from .models import Institution, Volume, Inventory, Congress, Session
from .models import OldAuth, OldInstitutions, OldInventory, OldServols

@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    pass


@admin.register(Volume)
class VolumeAdmin(admin.ModelAdmin):
    pass


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Congress)
class CongressAdmin(admin.ModelAdmin):
    pass


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    pass


@admin.register(OldAuth)
class OldAuthAdmin(admin.ModelAdmin):
    pass


@admin.register(OldInstitutions)
class OldInstitutionsAdmin(admin.ModelAdmin):
    pass


@admin.register(OldInventory)
class OldInventoryAdmin(admin.ModelAdmin):
    pass


@admin.register(OldServols)
class OldServolsAdmin(admin.ModelAdmin):
    pass
