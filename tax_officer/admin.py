from django.contrib import admin
from .models import Violation

# Register your models here.


@admin.register(Violation)
class ViolationAdmin(admin.ModelAdmin):
    list_display = (
        'driver_name', 'id', 'tax_officer',
        'car_number', 'location', 'cargo_type', 'cargo_date'
    )
    search_fields = (
        'tax_officer__full_name', 'driver_name',
        'driver_phone_number', 'car_number', 'location'
    )
    list_filter = ('tax_officer__full_name', 'cargo_type')
    ordering = ('created_at', 'id')
