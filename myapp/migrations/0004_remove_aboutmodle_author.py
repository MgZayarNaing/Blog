# Generated by Django 4.2.1 on 2024-01-22 16:31

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0003_aboutmodle"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="aboutmodle",
            name="author",
        ),
    ]