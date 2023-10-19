from rest_framework import serializers
from .models import (
    Listing,
    ADVERTISER_TYPE_CHOICES,
    OFFER_TYPE_CHOICES,
    PROPERTY_TYPE_CHOICES,
    LAND_AREA_UNIT_CHOICES,
    FURNISHING_STATUS_CHOICES,
)
from django.contrib.humanize.templatetags.humanize import intcomma, naturaltime
from django.utils.translation import gettext_lazy as _


class ListingSerializer(serializers.ModelSerializer):
    """
    Serializer for the Listing model.

    Transform Listing objects into JSON data for API responses.
    """

    advertizer = serializers.ReadOnlyField(source="accounts.username")
    is_owner = serializers.SerializerMethodField()
    advertizer_type = serializers.ChoiceField(
        choices=ADVERTISER_TYPE_CHOICES,
        style={"base_template": "radio.html"},
    )
    offer_type = serializers.ChoiceField(
        choices=OFFER_TYPE_CHOICES,
        style={"base_template": "radio.html"},
    )
    property_type = serializers.ChoiceField(
        choices=PROPERTY_TYPE_CHOICES,
        style={"base_template": "radio.html"},
    )
    floor_area = serializers.IntegerField(
        label=_("Floor Area (SqFt)")
    )
    land_area = serializers.IntegerField()
    land_area_unit = serializers.ChoiceField(
        choices=LAND_AREA_UNIT_CHOICES,
        style={"base_template": "radio.html"},
    )
    price = serializers.IntegerField(label=_("Price (Rs.)"))
    furnishing_status = serializers.ChoiceField(
        choices=FURNISHING_STATUS_CHOICES,
        style={"base_template": "radio.html"},
    )
    profile_id = serializers.ReadOnlyField(
        source="accounts.account.id"
    )
    profile_image = serializers.ReadOnlyField(
        source="accounts.account.image.url"
    )
    postal_code = serializers.ReadOnlyField()
    district = serializers.ReadOnlyField()
    created_at = serializers.ReadOnlyField()
    modified_at = serializers.ReadOnlyField()

    def to_representation(self, instance):
        """
        Transform the object into a JSON representation.
        """
        data = super().to_representation(instance)
        data["floor_area (in Sqft)"] = intcomma(instance.floor_area)
        data["land_area"] = intcomma(instance.land_area)
        data["price"] = intcomma(instance.price)
        data["created_at"] = naturaltime(instance.created_at)
        data["modified_at"] = naturaltime(instance.modified_at)
        return data

    def validate_image(self, value):
        """
        Validate the uploaded image size, width, and height.
        """
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError(
                "Image size larger than 2MB!"
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                "Image height larger than 4096px!"
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                "Image width larger than 4096px!"
            )
        return value

    def get_is_advertizer(self, obj):
        """
        Determine if the current user is the owner of the post.
        """
        request = self.context["request"]
        return request.user == obj.owner

    class Meta:
        model = Listing
        fields = (
            "id",
            "advertizer",
            "is_owner",
            "profile_id",
            "profile_image",
            "advertizer_type",
            "offer_type",
            "property_type",
            "address_no",
            "address_1",
            "address_2",
            "city",
            "postal_code",
            "district",
            "bedrooms",
            "bathrooms",
            "floor_area",
            "land_area",
            "land_area_unit",
            "furnishing_status",
            "price",
            "title",
            "description",
            "main_photo",
            "photo_1",
            "photo_2",
            "photo_3",
            "photo_4",
            "photo_5",
            "photo_6",
            "is_published",
            "created_at",
            "modified_at",
        )
