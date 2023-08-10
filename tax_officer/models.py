from django.db import models

# Create your models here.


class Profile(models.Model):
    full_name = models.CharField(
        verbose_name="Tax officer's name, surname, patronymic",
        max_length=150
    )
    passport_or_id_number = models.CharField(
        verbose_name="Passport or ID number",
        max_length=50
    )
    passport_or_id_file = models.FileField(
        verbose_name="Passport or ID file",
        upload_to="tax_officers/profile/"
    )
    position = models.CharField(
        verbose_name="The position of tax officer",
        max_length=100
    )
    working_region = models.CharField(
        verbose_name="Region of the tax officer",
        max_length=50
    )
    phone_number = models.CharField(
        verbose_name="Phone number of the tax officer",
        max_length=16
    )
    created_at = models.DateTimeField(
        verbose_name="Date of creation",
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Tax officer profile'
        verbose_name_plural = 'Tax officers profile'

    def __str__(self):
        return self.full_name


class Violation(models.Model):
    profile = models.ForeignKey(
        to=Profile,
        verbose_name="Tax officer's profile",
        related_name="violations",
        on_delete=models.CASCADE
    )
    driver_name = models.CharField(
        verbose_name="The name of the fined driver",
        max_length=150
    )
    driver_phone_number = models.CharField(
        verbose_name="The phone number of the fined driver",
        max_length=16
    )
    driver_passport_or_id_number = models.CharField(
        verbose_name="The passport or ID number of the fined driver",
        max_length=50
    )
    car_number = models.CharField(
        verbose_name="Fined driver car number",
        max_length=50
    )
    car_photo = models.FileField(
        verbose_name="Fined driver car photo",
        upload_to="tax_officers/violations/"
    )
    location = models.CharField(
        verbose_name="The location of the fined driver",
        max_length=100
    )
    cargo_type = models.CharField(
        verbose_name="Cargo type",
        max_length=100
    )
    date = models.DateField(
        verbose_name="Date of violation"
    )

    class Meta:
        verbose_name = 'Violation'
        verbose_name_plural = 'Violations'

    def __str__(self):
        return self.driver_name
