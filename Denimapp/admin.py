from django.contrib import admin
from Denimapp.models import DenimItems

class DenimAdmin(admin.ModelAdmin):
    list_display = ('denimImage','denimName','denimPrice','denimMrp','denimOffer','denimBestprice');


# Register your models here.
admin.site.register(DenimItems, DenimAdmin);