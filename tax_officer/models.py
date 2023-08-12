from django.db import models


DOCUMENT_TYPES = (
    ('passport', 'Passport'),
    ('document_id', 'ID')
)


REASON_VIOLATION = (
    ('not_entered', 'Ma\'lumot kiritilmagan'),
    ('entered_incorrect', 'Ma\'lumot notog\'ri kiritilgan')
)


class Violation(models.Model):
    tax_officer = models.ForeignKey(
        to="account.Account",
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
    location = models.CharField(
        verbose_name="The location of the fined driver",
        max_length=100
    )
    cargo_type = models.ForeignKey(
        to="karer.CargoType",
        verbose_name="Cargo type",
        on_delete=models.CASCADE,
        related_name="violations"
    )
    reason_violation = models.CharField(
        verbose_name="Reason violation",
        choices=REASON_VIOLATION,
        max_length=17,
        blank=True,
    )
    cargo_date = models.DateTimeField(
        verbose_name="The time the cargo was picked up"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Violation'
        verbose_name_plural = 'Violations'

    def __str__(self):
        return self.tax_officer.full_name
