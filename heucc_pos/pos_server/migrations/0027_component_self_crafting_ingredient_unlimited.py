# Generated by Django 4.2.9 on 2024-02-18 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos_server', '0026_dish_force_in_stock_alter_component_in_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='component',
            name='self_crafting',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='unlimited',
            field=models.BooleanField(default=False),
        ),
    ]