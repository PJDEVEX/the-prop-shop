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
        fields = "__all__"
