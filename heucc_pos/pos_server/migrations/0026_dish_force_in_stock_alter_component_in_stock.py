# Generated by Django 4.2.9 on 2024-02-14 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos_server', '0025_alter_component_inventory'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='force_in_stock',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='component',
            name='in_stock',
            field=models.BooleanField(default=False),
        ),
    ]