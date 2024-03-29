# Generated by Django 4.2 on 2023-08-14 07:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_account_is_phone_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, unique=True, validators=[django.core.validators.RegexValidator(message='Invalid phone number. Please enter in the format +998901234567 or 901234567', regex='^(\\+998|\\d{9})$')], verbose_name='phone number'),
        ),
    ]
