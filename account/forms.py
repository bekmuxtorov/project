from django.contrib.auth.forms import UserCreationForm as OldUserCreationForm, UserChangeForm as OldUserChangeForm

from .models import Account


class UserCreationForm(OldUserCreationForm):
    class Meta:
        model = Account
        fields = ("phone_number", "full_name")


class UserChangeForm(OldUserChangeForm):
    class Meta:
        model = Account
        fields = ("phone_number", "type", "full_name", "karer_name",
                  "password_or_id_number", "position", "working_region", "is_staff", "is_superuser")
