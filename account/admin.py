from django.contrib import admin
from .models import Account, Region
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(Account)
class AccountAdmin(BaseUserAdmin):
    list_display = ('username', 'full_name', 'type',
                    'phone_number', 'working_region')
    list_filter = ('type', 'working_region')
    search_fields = ('full_name', 'phone_number', 'position', 'karer_name')

    fieldsets = (
        (
            None,
            {
                "fields": (
                    'username', 'full_name', 'type',
                    'phone_number', 'working_region'
                )
            },
        ),
        (
            "Permissions",
            {"fields": ("is_staff", "is_superuser",
                        "groups", "user_permissions")},
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2"),
            },
        ),
    )
    ordering = ("username",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'get_count')
    search_fields = ('name',)

    def get_count(self, obj):
        return obj.accounts.count()
