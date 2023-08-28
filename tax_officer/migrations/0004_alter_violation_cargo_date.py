# Generated by Django 4.2 on 2023-08-28 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tax_officer', '0003_violation_stir_violation_who'),
    ]

    operations = [
        migrations.AlterField(
            model_name='violation',
            name='cargo_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='The time the cargo was picked up'),
        ),
    ]