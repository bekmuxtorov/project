# Generated by Django 4.2 on 2023-08-18 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karer', '0007_order_car_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='direction',
            field=models.CharField(blank=True, max_length=128, verbose_name='Direction'),
        ),
    ]