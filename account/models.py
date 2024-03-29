from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from rest_framework.authtoken.models import Token

from .managers import UserManager

DOCUMENT_TYPES = (
    ('passport', 'Passport'),
    ('document_id', 'ID')
)


ACCOUNT_TYPES = (
    ('karer', 'Karer'),
    ('tax_officer', 'Tax officer')
)


class TokenProxy(Token):
    class Meta:
        proxy = True
        verbose_name = "Token"
        verbose_name_plural = "Tokens"


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
        blank=True,
        validators=[
            RegexValidator(
                regex=r'^\+998\d{9}$',
                message='Invalid phone number. Please enter in the format +998901234567'
            ),
        ]
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
    working_region = models.CharField(
        verbose_name="Region",
        max_length=100,
        blank=True,
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
