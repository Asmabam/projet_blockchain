# Generated by Django 4.2.6 on 2023-12-18 16:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("students", "0005_student_diplom"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="diplom",
            field=models.FileField(blank=True, upload_to="students/diploms/"),
        ),
    ]
