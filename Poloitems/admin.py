from django.contrib import admin
from .models import Poloitems

class PoloAdmin(admin.ModelAdmin):
    list_display = ('poloImage', 'poloName', 'poloPrice', 'poloMrp', 'poloOffer', 'poloBestprice')

admin.site.register(Poloitems, PoloAdmin);
