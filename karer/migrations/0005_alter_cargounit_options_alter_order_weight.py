# Generated by Django 4.2 on 2023-08-15 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karer', '0004_rename_cargounity_cargounit_alter_cargounit_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cargounit',
            options={'verbose_name': 'Cargo unit', 'verbose_name_plural': 'Cargo units'},
        ),
        migrations.AlterField(
            model_name='order',
            name='weight',
            field=models.CharField(blank=True, max_length=150, verbose_name='Weight'),
        ),
    ]
