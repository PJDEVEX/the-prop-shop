import django_filters
from .models import Listing


class ListingFilter(django_filters.FilterSet):
    class Meta:
        model = Listing
        fields = {
            "offer_type": ["exact"],
            "property_type": ["exact"],
            "bedrooms": ["exact", "gte", "lte"],
            "bathrooms": ["exact", "gte", "lte"],
            "floor_area": ["exact", "gte", "lte"],
            "furnishing_status": ["exact"],
            "price": ["exact", "gte", "lte"],
            "address_1": ["icontains"],
            "address_2": ["icontains"],
            "city__name": ["icontains"],
            "district": ["icontains"],
        }
