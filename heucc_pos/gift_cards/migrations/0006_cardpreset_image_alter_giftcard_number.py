# Generated by Django 5.0.3 on 2024-05-14 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gift_cards', '0005_rename_cardpresets_cardpreset_alter_giftcard_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardpreset',
            name='image',
            field=models.ImageField(null=True, upload_to='files/gift-cards/presets'),
        ),
        migrations.AlterField(
            model_name='giftcard',
            name='number',
            field=models.CharField(default='0462000821517702', max_length=16),
        ),
    ]
