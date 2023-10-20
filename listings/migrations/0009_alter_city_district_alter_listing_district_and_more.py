# Generated by Django 4.2.5 on 2023-10-19 20:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("listings", "0008_rename_advertizer_listing_owner"),
    ]

    operations = [
        migrations.AlterField(
            model_name="city",
            name="district",
            field=models.CharField(max_length=55),
        ),
        migrations.AlterField(
            model_name="listing",
            name="district",
            field=models.CharField(max_length=20),
        ),
        migrations.DeleteModel(
            name="District",
        ),
    ]
