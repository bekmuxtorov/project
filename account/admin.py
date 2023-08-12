from django.contrib import admin
from .models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('username', 'full_name', 'id', 'type', 'phone_number', 'working_region')
    ordering = ('created_at', 'full_name', 'id')
    list_filter = ('type', 'working_region')
    search_fields = ('full_name', 'phone_number', 'position', 'karer_name')
