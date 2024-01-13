# Generated by Django 4.2.9 on 2024-01-12 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos_server', '0013_dishcomponent_componentingredient_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='componentingredient',
            name='quantity',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='dish',
            name='station',
            field=models.CharField(choices=[('bar', 'Bar'), ('kitchen', 'Kitchen')], max_length=50),
        ),
        migrations.AlterField(
            model_name='dishcomponent',
            name='quantity',
            field=models.FloatField(),
        ),
    ]
