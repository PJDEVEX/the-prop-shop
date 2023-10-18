from rest_framework import serializers
from .models import Listing


class ListingSerializer(serializers.ModelSerializer):
    """
    Serializer for the Listing model.

    This serializer is used to transform Listing model instances
    into JSON data and vice versa.

    Fields:
    - All fields from the Listing model.

    Usage Example:
    --------------
    To serialize a Listing object:
    serializer = ListingSerializer(listing_instance)
    serialized_data = serializer.data

    To deserialize JSON data into a Listing object:
    serializer = ListingSerializer(data=json_data)
    if serializer.is_valid():
        listing_instance = serializer.save()
    """

    class Meta:
        model = Listing
        fields = (
            'id',
            'advertizer',
            'advertizer_type',
            'offer_type',
            'property_type',
            'address_no',
            'address_1',
            'address_2',
            'city',
            'postal_code',
            'district',
            'bedrooms',
            'bathrooms',
            'floor_area',
            'land_area',
            'land_area_unit',
            'furnishing_status',
            'price',
            'title',
            'description',
            'main_photo',
            'photo_1',
            'photo_2',
            'photo_3',
            'photo_4',
            'photo_5',
            'photo_6',
            'is_published',
            'created_at',
            'modified_at',
        )
