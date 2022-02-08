from django.contrib import admin
from .models import MarketInformation, Asset
# Register your models here.


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    pass


@admin.register(MarketInformation)
class MarketInformationAdmin(admin.ModelAdmin):
    pass
