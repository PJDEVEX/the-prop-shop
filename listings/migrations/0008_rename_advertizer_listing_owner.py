# Generated by Django 4.2.5 on 2023-10-19 20:19

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "listings",
            "0007_alter_listing_bathrooms_alter_listing_is_published_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="listing",
            old_name="advertizer",
            new_name="owner",
        ),
    ]