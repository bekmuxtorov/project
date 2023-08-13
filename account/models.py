from .managers import UserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

DOCUMENT_TYPES = (
    ('passport', 'Passport'),
    ('document_id', 'ID')
)


ACCOUNT_TYPES = (
    ('karer', 'Karer'),
    ('tax_officer', 'Tax officer')
)


class Region(models.Model):
    name = models.CharField(
        verbose_name="Region",
        max_length=50
    )

    def __str__(self):
        return self.name


class Account(AbstractBaseUser, PermissionsMixin):
    type = models.CharField(
        choices=ACCOUNT_TYPES,
        default='karer',
        max_length=11
    )
    phone_number = models.CharField(
        verbose_name="phone number",
        max_length=20,
        unique=True,
        blank=True
    )
    full_name = models.CharField(
        verbose_name="Full name",
        max_length=100,
        blank=True
    )
    karer_name = models.CharField(
        verbose_name="Karer name",
        max_length=100,
        blank=True
    )
    passport_or_id = models.CharField(
        choices=DOCUMENT_TYPES,
        default='passport',
        max_length=11
    )
    password_or_id_number = models.CharField(
        verbose_name="Password or ID number",
        max_length=15,
        blank=True
    )
    position = models.CharField(
        verbose_name="Postion",
        max_length=50,
        blank=True
    )
    working_region = models.ForeignKey(
        to=Region,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="accounts"
    )
    sms_code = models.CharField(
        verbose_name="sms code",
        max_length=6,
        blank=True
    )
    is_phone_verified = models.BooleanField(
        verbose_name='Is phone verified',
        default=False
    )
    is_staff = models.BooleanField(
        verbose_name="is staff",
        default=False
    )
    created_at = models.DateTimeField(
        verbose_name="Date of creation",
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name="update profile",
        auto_now=True,
        blank=True,
        null=True
    )

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['full_name']

    objects = UserManager()

    def __str__(self):
        return self.phone_number
