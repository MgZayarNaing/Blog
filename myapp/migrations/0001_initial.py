# Generated by Django 4.2.1 on 2024-01-28 13:16

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
            ],
        ),
        migrations.CreateModel(
            name="ContactModel",
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
                ("firstname", models.CharField(blank=True, max_length=10, null=True)),
                ("lastname", models.CharField(blank=True, max_length=10, null=True)),
                ("email", models.EmailField(max_length=254)),
                ("subject", models.CharField(blank=True, max_length=500, null=True)),
                ("meassage", models.TextField()),
                ("created_at", models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
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
        migrations.CreateModel(
            name="BlogModel",
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
