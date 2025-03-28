# Generated by Django 5.0.1 on 2025-03-20 21:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bookings", "0002_apartment_price_per_day"),
    ]

    operations = [
        migrations.CreateModel(
            name="ResidentialComplex",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                ("address", models.CharField(max_length=255)),
                ("city", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True, null=True)),
                ("built_year", models.IntegerField(blank=True, null=True)),
                ("developer", models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name="apartment",
            name="description",
        ),
    ]
