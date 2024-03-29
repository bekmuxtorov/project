from django.contrib import admin
from .models import Order, CargoType, CargoUnit


@admin.register(CargoUnit)
class CargoUnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'created_at')
    ordering = ('created_at', )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'driver_name', 'unique_number', 'karer', 'cargo_type',
        'cargo_unit', 'car_number', 'location', 'status'
    )
    list_filter = ('cargo_type', 'karer__karer_name', 'cargo_unit')
    ordering = ('-date', '-id')
    search_fields = (
        'karer__karer_name', 'driver_name',
        'driver_phone_number', 'car_number', 'unique_number'
    )

    def delete_queryset(self, request, queryset) -> None:
        for obj in queryset:
            try:
                obj.car_photo.delete()
            except FileExistsError:
                pass
        return super().delete_queryset(request, queryset)
