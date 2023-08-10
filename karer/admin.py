from django.contrib import admin
from .models import Karer, Order

# Register your models here.


@admin.register(Karer)
class KarerAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'phone_number', 'user')
    ordering = ('name', 'id', 'phone_number')
    search_fields = ('name', 'phone_number')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('driver_name', 'id', 'karer',
                    'driver_phone_number', 'car_number', 'location')
    ordering = ('karer', 'driver_name')
    search_fields = ('karer__name', 'driver_name',
                     'driver_phone_number', 'car_number')
