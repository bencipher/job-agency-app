# Generated by Django 4.2 on 2023-04-23 22:33

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Job",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                (
                    "contract_type",
                    models.CharField(
                        choices=[("contract", "Contract"), ("permanent", "Permanent")],
                        max_length=255,
                    ),
                ),
                ("rate", models.DecimalField(decimal_places=2, max_digits=10)),
                ("location", models.CharField(max_length=255)),
                ("date_posted", models.DateField(auto_now_add=True)),
                ("is_cancelled", models.BooleanField(default=False)),
            ],
            options={
                "ordering": ("-date_posted",),
            },
        ),
    ]
