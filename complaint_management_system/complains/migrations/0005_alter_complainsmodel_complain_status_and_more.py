# Generated by Django 4.1.5 on 2023-02-27 13:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("complains", "0004_alter_complainsmodel_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="complainsmodel",
            name="complain_status",
            field=models.CharField(
                choices=[
                    ("PENDING", "PENDING"),
                    ("INITIALIZED", "INITIALIZED"),
                    ("RESOLVED", "RESOLVED"),
                    ("CONFIRMED", "CONFIRMED"),
                    ("FAILED", "FAILED"),
                ],
                default="INITIALIZED",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="complainsmodel",
            name="id",
            field=models.UUIDField(
                default=uuid.UUID("27085e61-9fa2-4140-9f51-badec32e7b21"),
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
    ]
