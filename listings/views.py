from rest_framework import generics, permissions
from django.db.models import Q
from .models import Listing
from .serializers import ListingSerializer
from drf_api.permissions import IsOwnerOrReadOnly


class ListingListCreateView(generics.ListCreateAPIView):
    """
    View for listing and creating property listings.

    This view allows users to list and create property listings.
    It supports the creation of new listings and listing existing ones.
    """

    serializer_class = ListingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Listing.objects.all()


class ListingRetrieveUpdateDestroyView(
    generics.RetrieveUpdateDestroyAPIView
):
    """
    View for retrieving, updating, and destroying property listings.

    This view allows users to retrieve, update, and delete property listings.
    It provides access to individual listing details and supports modifications
    or removal of listings.
    """

    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [IsOwnerOrReadOnly]
