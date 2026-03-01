from django.contrib import admin
from service.models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_icon', 'service_name', 'service_description');

admin.site.register(Service,ServiceAdmin);       #To register data in the admin panel

# Register your models here.
