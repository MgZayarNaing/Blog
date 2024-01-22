# Generated by Django 4.2.1 on 2024-01-22 15:27

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="HomeModel",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("img", models.ImageField(default=None, upload_to="")),
                ("title", models.CharField(blank=True, max_length=255, null=True)),
                ("contact", models.TextField(blank=True, null=True)),
                ("created_at", models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]