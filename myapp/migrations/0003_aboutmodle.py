# Generated by Django 4.2.1 on 2024-01-22 16:23

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("myapp", "0002_homemodel"),
    ]

    operations = [
        migrations.CreateModel(
            name="AboutModle",
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
                (
                    "author",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]