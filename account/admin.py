from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Account, Region
from .forms import UserChangeForm, UserCreationForm


@admin.register(Account)
class AccountAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = (
        "phone_number",
        "type",
        "created_at",
        "is_phone_verified",
        "is_staff"
    )
    list_filter = ("is_staff", "is_superuser",
                   "groups", "type", "working_region")
    fieldsets = (
        (
            "General data",
            {
                "fields": (
                    "type",
                    "phone_number",
                )
            },
        ),
        (
            "Karer",
            {
                "fields": (
                    "karer_name",
                )
            },
        ),
        (
            "Tax officer",
            {
                "fields": (
                    "full_name",
                    "passport_or_id",
                    "password_or_id_number",
                    "position",
                    "working_region",
                )
            },
        ),
        (
            "Permissions",
            {"fields": ("is_staff", "is_superuser",
                        "groups", "user_permissions")},
        ),
        ("Important dates", {
         "fields": ("last_login", 'sms_code', 'is_phone_verified')}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("type", "phone_number", "password1", "password2"),
            },
        ),
    )
    search_fields = ("phone_number", "chat_id", "full_name")
    ordering = ("type",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )

    def save_model(self, request, obj, form, change):
        if not change:
            obj.type = form.cleaned_data.get('type')
        super().save_model(request, obj, form, change)


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'get_count')
    search_fields = ('name',)

    def get_count(self, obj):
        return obj.accounts.count()
