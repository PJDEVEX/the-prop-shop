# Generated by Django 4.2.5 on 2023-10-20 21:21

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("listings", "0010_listing_phone_number_alter_listing_is_published"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("favorites", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="favorite",
            old_name="user",
            new_name="owner",
        ),
        migrations.AlterUniqueTogether(
            name="favorite",
            unique_together={("owner", "listing")},
        ),
    ]
