# Generated by Django 4.1.5 on 2023-02-24 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0007_alter_usermodel_password"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usermodel",
            name="date_of_birth",
            field=models.DateField(auto_now_add=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name="usermodel",
            name="gender",
            field=models.CharField(
                choices=[("M", "Male"), ("F", "Female")], default="M", max_length=6
            ),
        ),
    ]
