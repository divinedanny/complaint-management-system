# Generated by Django 4.1.5 on 2023-01-30 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("complains", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="complainsmodel",
            name="department",
            field=models.CharField(
                choices=[
                    ("admin", "administration"),
                    ("busary", "busary"),
                    ("security", "security"),
                    ("hall", "hall Adminstration"),
                    ("busa", "student Administration"),
                    ("bumu", "student Community Grade"),
                    ("registry", "registry"),
                    ("cafeteria", "Cafeteria"),
                ],
                max_length=30,
            ),
        ),
        migrations.AlterField(
            model_name="complainsmodel",
            name="matric_number",
            field=models.CharField(max_length=7),
        ),
    ]
