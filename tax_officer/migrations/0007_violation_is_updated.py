# Generated by Django 4.2 on 2023-08-21 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tax_officer', '0006_violation_car_brand_violation_karer_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='violation',
            name='is_updated',
            field=models.BooleanField(default=False, verbose_name='Is updated'),
        ),
    ]