# Generated by Django 4.2.6 on 2023-12-17 01:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("students", "0002_auto_20201124_0614"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="student",
            options={"ordering": ["surname", "firstname"]},
        ),
        migrations.RenameField(
            model_name="student",
            old_name="parent_mobile_number",
            new_name="mobile_number",
        ),
        migrations.RemoveField(
            model_name="student",
            name="current_status",
        ),
        migrations.RemoveField(
            model_name="student",
            name="date_of_admission",
        ),
        migrations.RemoveField(
            model_name="student",
            name="other_name",
        ),
        migrations.AlterField(
            model_name="student",
            name="address",
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name="student",
            name="gender",
            field=models.CharField(
                choices=[("homme", "Homme"), ("femme", "Femme")],
                default="male",
                max_length=10,
            ),
        ),
    ]
