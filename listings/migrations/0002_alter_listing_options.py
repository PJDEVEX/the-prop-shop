# Generated by Django 4.2.5 on 2023-10-17 20:22

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("listings", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="listing",
            options={"ordering": ["-created_at"]},
        ),
    ]