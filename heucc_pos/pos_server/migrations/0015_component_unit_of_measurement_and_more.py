# Generated by Django 4.2.9 on 2024-01-12 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos_server', '0014_alter_componentingredient_quantity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='component',
            name='unit_of_measurement',
            field=models.CharField(choices=[('kg', 'Kilogram'), ('g', 'Gram'), ('l', 'Liter'), ('ml', 'Milliliter'), ('ea', 'Each')], default='kg', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ingredient',
            name='unit_of_measurement',
            field=models.CharField(choices=[('kg', 'Kilogram'), ('g', 'Gram'), ('l', 'Liter'), ('ml', 'Milliliter'), ('ea', 'Each')], default='kg', max_length=10),
            preserve_default=False,
        ),
    ]
