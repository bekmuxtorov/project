from django.db import models
from django.contrib.auth.models import User

# Create your models here.

DOCUMENT_TYPES = (
    ('passport', 'Passport'),
    ('document_id', 'ID')
)


class CargoType(models.Model):
    name = models.CharField(
        verbose_name="Cargo Type",
        max_length=50
    )
    created_at = models.DateTimeField(auto_now_add=True)

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
    car_photo = models.FileField(
        verbose_name="Car photo",
        upload_to="orders/car/"
    )
    location = models.CharField(
        verbose_name="Location",
        max_length=150
    )
    cargo_type = models.ForeignKey(
        to=CargoType,
        on_delete=models.CASCADE,
        related_name='orders',
    )
    weight = models.CharField(
        verbose_name="Weight",
        max_length=150
    )
    date = models.DateField(
        auto_now_add=True
    )

    def __str__(self) -> str:
        return self.driver_name
