# Generated by Django 4.2.9 on 2024-01-14 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos_server', '0015_component_unit_of_measurement_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='special_instructions',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='table',
            field=models.CharField(max_length=140, null=True),
        ),
    ]