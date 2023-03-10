# Generated by Django 4.1.3 on 2023-03-06 22:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("complains", "0002_alter_complainsmodel_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="complainsmodel",
            name="id",
            field=models.UUIDField(
                default=uuid.UUID("850f341e-38f6-4bec-874e-62ff233dee4c"),
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
    ]
