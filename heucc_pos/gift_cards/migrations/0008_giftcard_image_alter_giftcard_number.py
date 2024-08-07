# Generated by Django 5.0.3 on 2024-06-06 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gift_cards', '0007_specialcard_alter_giftcard_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='giftcard',
            name='image',
            field=models.ImageField(null=True, upload_to='files/gift-cards/presets'),
        ),
        migrations.AlterField(
            model_name='giftcard',
            name='number',
            field=models.CharField(default='8183133500825011', max_length=16),
        ),
    ]
