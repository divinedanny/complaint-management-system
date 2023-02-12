# Generated by Django 4.1.5 on 2023-02-03 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("complains", "0003_complainsmodel_complain_state"),
    ]

    operations = [
        migrations.AlterField(
            model_name="complainsmodel",
            name="complain_state",
            field=models.CharField(
                choices=[
                    ("NOT SUBMITTED", "NOT SUBMITTEED"),
                    ("SUBMITTED", "SUBMITTED"),
                    ("INITIALIZED", "INITIALIZED"),
                    ("RESOLVED", "RESOLVED"),
                    ("CONFIRMED", "CONFIRMED"),
                    ("FAILED", "FAILED"),
                    ("COMPLETED", "COMPLETED"),
                    ("START", "START"),
                ],
                default="START",
                max_length=20,
            ),
        ),
    ]