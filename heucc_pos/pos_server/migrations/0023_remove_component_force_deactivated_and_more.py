# Generated by Django 4.2.9 on 2024-02-09 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos_server', '0022_component_force_deactivated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='component',
            name='force_deactivated',
        ),
        migrations.AddField(
            model_name='component',
            name='in_stock',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dish',
            name='in_stock',
            field=models.BooleanField(default=True),
        ),
    ]