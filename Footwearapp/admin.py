from django.contrib import admin
from Footwearapp.models import FootwearItems

class FootwearAdmin(admin.ModelAdmin):
    list_display = ('footwearImage','footwearName','footwearPrice','footwearMrp','footwearOffer','footwearBestprice');

# Register your models here.
admin.site.register(FootwearItems, FootwearAdmin);
