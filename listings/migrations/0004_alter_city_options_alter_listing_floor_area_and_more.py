# Generated by Django 4.2.5 on 2023-10-18 20:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("listings", "0003_alter_listing_description"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="city",
            options={"ordering": ["name"], "verbose_name_plural": "cities"},
        ),
        migrations.AlterField(
            model_name="listing",
            name="floor_area",
            field=models.IntegerField(verbose_name="Floor Area (SqFt)"),
        ),
        migrations.AlterField(
            model_name="listing",
            name="price",
            field=models.IntegerField(verbose_name="Price (Rs.)"),
        ),
    ]
