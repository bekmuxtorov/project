# Generated by Django 4.2 on 2023-08-18 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_tokenproxy_alter_account_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='working_region',
            field=models.CharField(blank=True, max_length=100, verbose_name='Region'),
        ),
    ]
