# Generated by Django 4.2 on 2023-08-27 14:52

from django.db import migrations, models
import karer.models


class Migration(migrations.Migration):

    dependencies = [
        ('karer', '0002_alter_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='unique_number',
            field=models.IntegerField(blank=True, default=karer.models.create_new_ref_number),
        ),
    ]
