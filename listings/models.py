from django.db import models
from accounts.models import Account
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from .addresses_choices import city_dict
import phonenumbers

# Choices for different fields
ADVERTISER_TYPE_CHOICES = [
    ("owner", "Owner"),
    ("agent", "Agent"),
]

OFFER_TYPE_CHOICES = [
    ("sale", "Sale"),
    ("rent", "Rent"),
]

PROPERTY_TYPE_CHOICES = [
    ("house", "House"),
    ("apartment", "Apartment"),
    ("bungalow", "Bungalow"),
    ("villa", "Villa"),
    ("annexe", "Annexe"),
    ("rooms", "Rooms"),
    ("studio", "Studio"),
]

LAND_AREA_UNIT_CHOICES = [
    ("perches", "Perches"),
    ("acres", "Acres"),
]

FURNISHING_STATUS_CHOICES = [
    ("unfurnished", "Unfurnished"),
    ("basic_furnished", "Basic Furnished"),
    ("modern_furnished", "Modern Furnished"),
    ("fully_furnished", "Fully Furnished"),
    ("custom_furnished", "Custom Furnished"),
]


class City(models.Model):
    """Model to represent cities."""

    name = models.CharField(max_length=55)
    district = models.CharField(max_length=55)
    postal_code = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = "cities"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Listing(models.Model):
    """Model to represent property listings."""

    owner = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name="listings",
    )
    advertizer_type = models.CharField(
        max_length=10,
        choices=ADVERTISER_TYPE_CHOICES,
        default="owner",
    )
    offer_type = models.CharField(
        max_length=10, choices=OFFER_TYPE_CHOICES, default="sale"
    )
    property_type = models.CharField(
        max_length=10, choices=PROPERTY_TYPE_CHOICES, default="house"
    )
    address_no = models.CharField(max_length=10)
    address_1 = models.CharField(max_length=55)
    address_2 = models.CharField(max_length=55)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    postal_code = models.CharField(max_length=10)
    district = models.CharField(max_length=20)
    phone_number = models.CharField(
        max_length=20,
        help_text="Contact phone number",
        null=True,
        blank=True,
    )
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField(blank=True)
    floor_area = models.IntegerField(_("Floor Area (SqFt)"))
    land_area = models.IntegerField(blank=True)
    land_area_unit = models.CharField(
        max_length=10,
        choices=LAND_AREA_UNIT_CHOICES,
        blank=True,
    )
    furnishing_status = models.CharField(
        max_length=25,
        choices=FURNISHING_STATUS_CHOICES,
        null=True,
        blank=True,
    )
    price = models.IntegerField(_("Price (Rs.)"))
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=3000)
    main_photo = models.ImageField(upload_to="images/")
    photo_1 = models.ImageField(
        upload_to="images/", blank=True, null=True
    )
    photo_2 = models.ImageField(
        upload_to="images/", blank=True, null=True
    )
    photo_3 = models.ImageField(
        upload_to="images/", blank=True, null=True
    )
    photo_4 = models.ImageField(
        upload_to="images/", blank=True, null=True
    )
    photo_5 = models.ImageField(
        upload_to="images/", blank=True, null=True
    )
    photo_6 = models.ImageField(
        upload_to="images/", blank=True, null=True
    )
    is_published = models.BooleanField(
        default=False,
        help_text="""
    Please review your listing details for accuracy
    before publishing. Ensure all information is complete
    and correct. Thank you.
""",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def get_advertiser_type_display(self):
        """Return the display value of the advertiser type."""
        return dict(ADVERTISER_TYPE_CHOICES).get(
            self.advertiser_type, "Owner"
        )

    def get_offer_type_display(self):
        """Return the display value of the offer type."""
        return dict(OFFER_TYPE_CHOICES).get(self.offer_type, "Sale")

    def get_property_type_display(self):
        """Return the display value of the property type."""
        return dict(PROPERTY_TYPE_CHOICES).get(
            self.property_type, "House"
        )

    def get_full_address(self):
        """Return the full address as a single line."""
        full_address = (
            f"{self.address_no}, {self.address_1}, "
            f"{self.address_2}, {self.city}"
        )

        return full_address

    def clean_phone_number(self):
        """
        Validate and format the phone number using phonenumbers package.
        """
        if self.phone_number:
            try:
                parsed_number = phonenumbers.parse(
                    self.phone_number, None
                )
                if not phonenumbers.is_valid_number(parsed_number):
                    raise ValidationError("Invalid phone number")
                self.phone_number = phonenumbers.format_number(
                    parsed_number, phonenumbers.PhoneNumberFormat.E164
                )
            except phonenumbers.phonenumberutil.NumberFormatError:
                raise ValidationError("Invalid phone number")

    def save(self, *args, **kwargs):
        """
        populate postal code and district.
        """
        if self.city:
            city_data = city_dict.get(self.city.name)
            if city_data:
                self.postal_code = city_data["postal_code"]
                self.district = city_data["district"]
        super().save(*args, **kwargs)

    def delete(self):
        """Custom delete method to delete associated photos."""
        self.main_photo.storage.delete(self.main_photo.name)
        self.photo_1.storage.delete(self.photo_1.name)
        self.photo_2.storage.delete(self.photo_2.name)
        self.photo_3.storage.delete(self.photo_3.name)
        self.photo_4.storage.delete(self.photo_4.name)
        self.photo_5.storage.delete(self.photo_5.name)
        self.photo_6.storage.delete(self.photo_6.name)
        super().delete()

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        """
        Return the title of the listing.
        """
        return self.title
