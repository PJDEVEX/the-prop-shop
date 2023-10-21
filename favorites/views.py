from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from favorites.models import Favorite
from favorites.serializers import FavoriteSerializer
from listings.serializers import ListingSerializer
from listings.models import Listing


class FavoriteListCreate(generics.ListCreateAPIView):
    """
    List Favorite or create a Favorite if user is logged in.
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = FavoriteSerializer
    queryset = Favorite.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserFavoriteListView(generics.ListAPIView):
    """
    List favorite listings of the currently authenticated user.
    """

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ListingSerializer

    def get_queryset(self):
        user = self.request.user
        favorites = Favorite.objects.filter(owner=user)
        listing_ids = [favorite.listing.id for favorite in favorites]
        return Listing.objects.filter(id__in=listing_ids)


class FavoriteRetrieveDestroy(generics.RetrieveDestroyAPIView):
    """
    Retrieve a favorite or delete it by id if you own it.
    """

    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = FavoriteSerializer
    queryset = Favorite.objects.all()
