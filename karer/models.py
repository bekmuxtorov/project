from django.db import models
from django.contrib.auth.models import User
import random


DOCUMENT_TYPES = (
    ('passport', 'Passport'),
    ('document_id', 'ID')
)


def create_new_ref_number():
    not_unique = True
    while not_unique:
        unique_ref = random.randint(100000, 999999)
        if not Order.objects.filter(unique_number=unique_ref):
            not_unique = False
            return unique_ref


class CargoType(models.Model):
    name = models.CharField(
        verbose_name="Cargo Type",
        max_length=50
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class CargoUnit(models.Model):
    name = models.CharField(
        verbose_name="Name",
        max_length=50,
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Cargo unit'
        verbose_name_plural = 'Cargo units'

    def __str__(self):
        return self.name


class Order(models.Model):
    karer = models.ForeignKey(
        to='account.Account',
        verbose_name="Karer",
        related_name="orders",
        on_delete=models.CASCADE
    )
    driver_name = models.CharField(
        verbose_name="Driver's name",
        max_length=150
    )
    driver_phone_number = models.CharField(
        verbose_name="Driver's phone number",
        max_length=16
    )
    driver_passport_or_id = models.CharField(
        choices=DOCUMENT_TYPES,
        default='passport',
        max_length=11
    )
    driver_passport_or_id_number = models.CharField(
        verbose_name="Driver's passport or ID number",
        max_length=50
    )
    car_number = models.CharField(
        verbose_name="Car number",
        max_length=50
    )
    car_photo = models.ImageField(
        verbose_name="Car photo",
        upload_to="orders/car/"
    )
    car_brand = models.CharField(
        verbose_name="Car brand",
        max_length=100,
        blank=True
    )
    trailer = models.CharField(
        verbose_name="Trailer",
        max_length=100,
        blank=True
    )
    trailer_weight = models.DecimalField(
        verbose_name="Trailer weight",
        decimal_places=2,
        max_digits=15,
        blank=True,
        null=True
    )
    direction = models.CharField(
        verbose_name="Direction",
        max_length=128,
        blank=True
    )
    location = models.CharField(
        verbose_name="Location",
        max_length=150
    )
    cargo_type = models.CharField(
        verbose_name="Cargo type",
        max_length=100,
        blank=True
    )
    cargo_unit = models.ForeignKey(
        to=CargoUnit,
        on_delete=models.CASCADE,
        related_name='orders',
        blank=True,
        null=True
    )
    cargo_value = models.DecimalField(
        verbose_name="Cargo value",
        decimal_places=2,
        max_digits=15,
        blank=True,
        null=True
    )
    status = models.CharField(
        verbose_name="Status Order",
        max_length=100,
        blank=True
    )
    violated = models.BooleanField(
        verbose_name="Violated",
        default=False
    )
    stir = models.CharField(
        verbose_name="Stir",
        max_length=100,
        blank=True
    )
    who = models.CharField(
        verbose_name="Who",
        max_length=100,
        blank=True
    )
    date = models.DateTimeField(
        auto_now_add=True
    )
    unique_number = models.IntegerField(
        blank=True,
        default=create_new_ref_number
    )

    def __str__(self) -> str:
        return self.driver_name

    def delete(self, *args, **kwargs):
        if self.car_photo:
            self.car_photo.delete()
        super().delete(*args, **kwargs)
