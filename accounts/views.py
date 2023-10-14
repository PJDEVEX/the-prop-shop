import requests
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_api.permissions import IsOwnerOrReadOnly
from .serializers import (
    RegistrationSerializer,
    UsersSerializer,
    UserDetailSerializer,
)
from rest_framework import permissions
from .models import Account


class CreateAccount(APIView):
    """
    API endpoint for user registration.

    This view allows new users to register an account.

    Permission Classes:
    - AllowAny: Open to anyone, no authentication required.

    HTTP Methods:
    - POST: Create a new user account.

    Request Data:
    - email: User's email address.
    - password: User's password.

    Response:
    - If successful, returns a token for authentication.
    - If there's an error, returns a bad request response.

    """

    permission_classes = [permissions.AllowAny]

    def post(self, request):
        """
        Create a new user account.

        Request Data:
        - email: User's email address.
        - password: User's password.

        Returns:
        - If successful, returns a token for authentication.
        - If there's an error, returns a bad request response.

        """
        reg_serializer = RegistrationSerializer(data=request.data)
        if reg_serializer.is_valid():
            new_user = reg_serializer.save()
            if new_user:
                r = requests.post(
                    "https://8000-pjdevex-thepropshop-fhncw5hdrsb.ws-eu105.gitpod.io/api-auth/token",
                    data={
                        "username": new_user.email,
                        "password": request.data["password"],
                        "client_id": "Your Client ID",
                        "client_secret": "Your Client Secret",
                        "grant_type": "password",
                    },
                )
                return Response(
                    r.json(), status=status.HTTP_201_CREATED
                )
        return Response(
            reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


class AllUsers(generics.ListAPIView):
    """
    API endpoint to retrieve a list of all users.

    This view allows anyone to retrieve a list of all users.

    Permission Classes:
    - AllowAny: Open to anyone, no authentication required.

    HTTP Methods:
    - GET: Retrieve a list of all users.

    Response:
    - Returns a list of user information.

    """

    permission_classes = [permissions.AllowAny]
    queryset = Account.objects.all()
    serializer_class = UsersSerializer


class CurrentUser(APIView):
    """
    API endpoint to retrieve info about the currently authenticated user.

    Permission Classes:
    - IsAuthenticated: Requires authentication for access.

    HTTP Methods:
    - GET: Retrieve user information for the currently authenticated user.

    Response:
    - Returns user information for the authenticated user.

    """

    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        """
        Retrieve user information for the currently authenticated user.

        Returns:
        - User information for the currently authenticated user.

        """
        serializer = UsersSerializer(
            self.request.user, context={"request": request}
        )
        return Response(serializer.data)


class UserDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve and update the details of a user account if you are the owner.

    The view allows authenticated users to retrieve and update account details.
    Users are only authorized to access and modify their own account info.

    Permission Classes:
    - IsOwnerOrReadOnly: Only the owner of the account can update details.

    HTTP Methods:
    - GET: Retrieve the user's account details.
    - PUT/PATCH: Update the user's account details.

    Successful Response (HTTP 200):
    - Returns a JSON object containing the user's account information.

    Error Responses:
    - HTTP 404 (Not Found): If the requested user's account does not exist.
    - HTTP 500 (Internal Server Error): For unexpected server errors.

    """

    queryset = Account.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        except Account.DoesNotExist:
            return Response(
                {"error": "User not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as e:
            # Handle unexpected exceptions, return a custom error response
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
