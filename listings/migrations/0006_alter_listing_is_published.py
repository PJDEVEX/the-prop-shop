# Generated by Django 4.2.5 on 2023-10-19 10:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("listings", "0005_alter_listing_advertizer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="listing",
            name="is_published",
            field=models.BooleanField(
                default=False,
                help_text="Please review your listing details for accuracy before publishing.\nEnsure all information is complete and correct.\nThank you.",
            ),
        ),
    ]