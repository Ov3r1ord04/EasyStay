# Generated by Django 5.0.1 on 2025-03-25 02:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0011_alter_user_date_joined"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="age",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
