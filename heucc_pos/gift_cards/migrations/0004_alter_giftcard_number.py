# Generated by Django 5.0.3 on 2024-05-11 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gift_cards', '0003_alter_giftcard_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='giftcard',
            name='number',
            field=models.CharField(default='8329553739864659', max_length=16),
        ),
    ]
