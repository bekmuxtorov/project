from django.db import models
import random


DOCUMENT_TYPES = (
    ('passport', 'Passport'),
    ('document_id', 'ID')
)


def create_new_ref_number():
    not_unique = True
    while not_unique:
        unique_ref = random.randint(100000, 999999)
        if not Violation.objects.filter(unique_number=unique_ref):
            not_unique = False
            return unique_ref


class Violation(models.Model):
    tax_officer = models.ForeignKey(
        to="account.Account",
        verbose_name="Tax officer's profile",
        related_name="violations",
        on_delete=models.CASCADE
    )
    karer_name = models.CharField(
        verbose_name="Karer name",
        max_length=100,
        blank=True
    )
    driver_name = models.CharField(
        verbose_name="The name of the fined driver",
        max_length=150
    )
    driver_phone_number = models.CharField(
        verbose_name="The phone number of the fined driver",
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
        verbose_name="Fined driver car number",
        max_length=50
    )
    car_photo = models.FileField(
        verbose_name="Fined driver car photo",
        upload_to="tax_officers/violations/"
    )
    car_brand = models.CharField(
        verbose_name="Car brand",
        max_length=100,
        blank=True
    )
    location = models.CharField(
        verbose_name="The location of the fined driver",
        max_length=100
    )
    cargo_type = models.CharField(
        verbose_name="Cargo type",
        max_length=100,
        blank=True
    )
    reason_violation = models.CharField(
        verbose_name="Reason violation",
        max_length=100,
        blank=True,
    )
    is_updated = models.BooleanField(
        verbose_name="Is updated",
        default=False
    )
    cargo_date = models.DateTimeField(
        verbose_name="The time the cargo was picked up"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    unique_number = models.IntegerField(
        blank=True,
        default=create_new_ref_number
    )

    class Meta:
        verbose_name = 'Violation'
        verbose_name_plural = 'Violations'

    def __str__(self):
        return self.tax_officer.full_name

    def delete(self, *args, **kwargs):
        if self.car_photo:
            self.car_photo.delete()
        super().delete(*args, **kwargs)
