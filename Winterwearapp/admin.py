from django.contrib import admin
from Winterwearapp.models import Winterwearitems

class WinterwearAdmin(admin.ModelAdmin):
    list_display = ('winterwearImage','winterwearName','winterwearPrice','winterwearMrp','winterwearOffer','winterwearBestprice');


# Register your models here.
admin.site.register(Winterwearitems, WinterwearAdmin);

# Register your models here.
