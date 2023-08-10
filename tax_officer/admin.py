from django.contrib import admin
from .models import Profile, Violation

# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'id', 'position',
                    'working_region', 'phone_number')
    ordering = ('-created_at', 'full_name')
    search_fields = ('full_name', 'position', 'working_region', 'phone_number')


@admin.register(Violation)
class ViolationAdmin(admin.ModelAdmin):
    list_display = ('driver_name', 'id',
                    'driver_phone_number', 'car_number', 'location', 'cargo_type', 'date')
    search_fields = ('profile__full_name', 'driver_name',
                     'driver_phone_number', 'car_number', 'location')
