# Generated by Django 4.2 on 2023-04-24 22:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_rename_status_organization_still_exist_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="organization",
            name="name",
            field=models.CharField(max_length=255),
        ),
    ]
