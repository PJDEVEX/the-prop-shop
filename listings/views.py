from rest_framework import status, permissions
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Listing
from .serializers import ListingSerializer
from drf_api.permissions import IsOwnerOrReadOnly


# Define the calculate_listing_priority function here
def calculate_listing_priority(listing):
    photo_count = sum(1 for field in listing._meta.get_fields() if field.name.startswith('photo_') and getattr(listing, field.name))
    description_word_count = len(listing.description.split())
    
    # Define your priority calculation logic here. This is just a simple example.
    if photo_count > 4 and description_word_count > 150:
        return 0.7  # High priority
    else:
        return 0.3  # Lower priority

class ListingListCreateView(APIView):
    """
    API view for listing creation and retrieval.
    """

    serializer_class = ListingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        """
        Retrieve a list of all listings, sorted by priority.

        Retrieves and returns a list of all available listings, sorted by priority.

        Args:
            request: HTTP request object.

        Returns:
            Response: JSON response containing the list of listings.
        """
        listings = Listing.objects.all()
        
        # Sort the listings based on priority
        sorted_listings = sorted(listings, key=calculate_listing_priority, reverse=True)
        
        serializer = ListingSerializer(
            sorted_listings, many=True, context={"request": request}
        )
        return Response(serializer.data)

    def post(self, request):
        """
        Create a new listing.

        Creates a new listing based on the data provided in the request.

        Args:
            request: HTTP request object.

        Returns:
            Response: JSON response containing the created listing or
            validation errors.
        """
        serializer = ListingSerializer(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )



class ListingRetrieveUpdateDestroyView(APIView):
    """
    API view for retrieving, updating, and deleting listings.
    """

    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ListingSerializer

    def get_object(self, pk):
        """
        Get a listing by its primary key.

        Retrieves a listing based on its primary key.

        Args:
            pk: Primary key of the listing.

        Returns:
            Listing: The retrieved listing.

        Raises:
            Http404: If the listing with the given primary key does not exist.
        """
        try:
            listing = Listing.objects.get(pk=pk)
            self.check_object_permissions(self.request, listing)
            return listing
        except Listing.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """
        Retrieve a listing.

        Retrieves and returns the details of a single listing.

        Args:
            request: HTTP request object.
            pk: Primary key of the listing.

        Returns:
            Response: JSON response containing the details of the listing.
        """
        listing = self.get_object(pk)
        serializer = ListingSerializer(
            listing, context={"request": request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        """
        Update a listing.

        Updates the details of a single listing based on the provided data.

        Args:
            request: HTTP request object.
            pk: Primary key of the listing.

        Returns:
            Response: JSON response containing the updated listing or
            validation errors.
        """
        listing = self.get_object(pk)
        serializer = ListingSerializer(
            listing, data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        """
        Delete a listing.

        Deletes a single listing based on its primary key.

        Args:
            request: HTTP request object.
            pk: Primary key of the listing.

        Returns:
            Response: HTTP response indicating a successful deletion.
        """
        listing = self.get_object(pk)
        listing.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
