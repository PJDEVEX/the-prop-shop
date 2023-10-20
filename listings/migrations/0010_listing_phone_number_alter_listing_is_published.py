# Generated by Django 4.2.5 on 2023-10-20 17:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("listings", "0009_alter_city_district_alter_listing_district_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="listing",
            name="phone_number",
            field=models.CharField(
                blank=True, help_text="Contact phone number", max_length=20, null=True
            ),
        ),
        migrations.AlterField(
            model_name="listing",
            name="is_published",
            field=models.BooleanField(
                default=False,
                help_text="\n    Please review your listing details for accuracy\n    before publishing. Ensure all information is complete\n    and correct. Thank you.\n",
            ),
        ),
    ]