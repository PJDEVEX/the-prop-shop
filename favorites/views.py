from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from favorites.models import Favorite
from favorites.serializers import FavoriteSerializer


class FavoriteListCreate(generics.ListCreateAPIView):
    """
    List Favorite or create a Favorite if user is logged in.
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = FavoriteSerializer
    queryset = Favorite.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FavoriteRetrieveDestroy(generics.RetrieveDestroyAPIView):
    """
    Retrieve a favorite or delete it by id if you own it.
    """

    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = FavoriteSerializer
    queryset = Favorite.objects.all()
