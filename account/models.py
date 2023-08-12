from django.db import models
from django.contrib.auth.models import AbstractUser

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


class Account(AbstractUser):
    type = models.CharField(
        choices=ACCOUNT_TYPES,
        default='karer',
        max_length=11
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
    phone_number = models.CharField(
        verbose_name="Phone Number",
        max_length=20,
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
    created_at = models.DateTimeField(
        verbose_name="Date of creation",
        auto_now_add=True
    )

    def __str__(self):
        return self.username
