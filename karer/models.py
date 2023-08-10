from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Karer(models.Model):
    name = models.CharField(
        verbose_name="Karer's name",
        max_length=150
    )
    phone_number = models.CharField(
        verbose_name="Karer's phone number",
        max_length=16
    )
    user = models.OneToOneField(
        to=User,
        verbose_name="User",
        related_name="karer",
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Karer'
        verbose_name_plural = 'Karers'

    def __str__(self):
        return self.name


class Order(models.Model):
    karer = models.ForeignKey(
        to=Karer,
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
    driver_passport_or_id_file = models.FileField(
        verbose_name="Driver's passport or ID file",
        upload_to="orders/driver/"
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
    cargo_type = models.CharField(
        verbose_name="Cargo type",
        max_length=150
    )
    weight = models.CharField(
        verbose_name="Weight",
        max_length=150
    )
    date = models.DateField(
        verbose_name="Date of order"
    )

    def __str__(self) -> str:
        return self.driver_name
