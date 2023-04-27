# Generated by Django 4.2 on 2023-04-25 08:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_alter_organization_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="email",
            field=models.EmailField(blank=True, max_length=30, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="first_name",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="last_name",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]