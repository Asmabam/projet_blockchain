# Generated by Django 4.2.6 on 2023-12-18 14:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("students", "0004_rename_registration_number_student_identifiant"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="diplom",
            field=models.FileField(blank=True, upload_to="students/passports/"),
        ),
    ]