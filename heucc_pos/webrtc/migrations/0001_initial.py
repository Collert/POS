# Generated by Django 4.2.8 on 2023-12-20 17:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebRTCSession',
            fields=[
                ('session_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('offer', models.TextField(blank=True, null=True)),
                ('answer', models.TextField(blank=True, null=True)),
                ('ice_candidates', models.TextField(blank=True, null=True)),
            ],
        ),
    ]