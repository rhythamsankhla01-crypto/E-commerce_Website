from django.contrib import admin
from fresharrivals.models import freshArrivals

class FreshAdmin(admin.ModelAdmin):
    list_display = ('freshTitle', 'freshMrp', 'freshPrice', 'freshOffer', 'freshbestprice')
    list_editable = ('freshMrp', 'freshPrice', 'freshOffer', 'freshbestprice')
    search_fields = ('freshTitle',)
    list_filter = ('freshOffer',)

admin.site.register(freshArrivals, FreshAdmin);

