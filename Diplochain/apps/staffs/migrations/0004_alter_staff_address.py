# Generated by Django 4.2.6 on 2023-12-16 22:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("staffs", "0003_remove_staff_date_of_admission_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="staff",
            name="address",
            field=models.CharField(blank=True, max_length=30),
        ),
    ]