from django.contrib import admin
from Reviewsapp.models import Reviews


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('PersonName','Description');
# Register your models here.

admin.site.register(Reviews, ReviewsAdmin);