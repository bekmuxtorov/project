from django.contrib import admin
from .models import Order, CargoType


@admin.register(CargoType)
class CargoTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name', )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'driver_name', 'id', 'karer', 'cargo_type',
        'driver_phone_number', 'car_number', 'location'
    )
    list_filter = ('cargo_type__name', 'karer__karer_name')
    ordering = ('date', 'id')
    search_fields = (
        'karer__karer_name', 'driver_name',
        'driver_phone_number', 'car_number'
    )
