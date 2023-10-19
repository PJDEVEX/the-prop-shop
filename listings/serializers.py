from rest_framework import serializers
from .models import Listing


class ListingSerializer(serializers.ModelSerializer):
    advertizer = serializers.ReadOnlyField(source="accounts.username")
    is_owner = serializers.SerializerMethodField()
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
        Method to determine if the current user is the owner of the post.
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
