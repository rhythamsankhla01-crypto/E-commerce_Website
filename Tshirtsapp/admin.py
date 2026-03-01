from django.contrib import admin
from Tshirtsapp.models import Tshirt

class tshirtAdmin(admin.ModelAdmin):
    list_display = ('tshirtImage', 'tshirtName', 'tshirtPrice', 'tshirtMrp', 'tshirtOffer', 'tshirtBestprice')

admin.site.register(Tshirt, tshirtAdmin);
# Register your models here.
