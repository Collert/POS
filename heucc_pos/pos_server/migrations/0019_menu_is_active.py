# Generated by Django 4.2.9 on 2024-01-22 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos_server', '0018_menu_accent_1_menu_accent_2_menu_accent_3_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
