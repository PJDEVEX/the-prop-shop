from django.db.models import Q
from rest_framework import status, permissions
from django.http import Http404
from rest_framework.response import Response
from rest_framework import generics
from .models import Listing
from .serializers import ListingSerializer
from drf_api.permissions import IsOwnerOrReadOnly
from .filters import ListingFilter
from django_filters.rest_framework import DjangoFilterBackend


def calculate_listing_priority(listing):
    """
    Calculate the priority of a listing based on
    the number of photos and description length.
    """
    photo_count = sum(
        1
        for field in listing._meta.get_fields()
        if field.name.startswith("photo_")
        and getattr(listing, field.name)
    )
    description_word_count = len(listing.description.split())

    if photo_count > 4 and description_word_count > 150:
        return 0.7
    else:
        return 0.3


class ListingListCreateView(generics.ListCreateAPIView):
    """
    API view for listing creation and retrieval.
    """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ListingFilter

    def get(self, request, *args, **kwargs):
        listings = self.filter_queryset(self.get_queryset())
        sorted_listings = sorted(listings, key=calculate_listing_priority, reverse=True)
        serializer = ListingSerializer(sorted_listings, many=True, context={"request": request})
        return Response(serializer.data)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ListingRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [IsOwnerOrReadOnly]
