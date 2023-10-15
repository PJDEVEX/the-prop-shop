import requests
from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied, NotFound
from django.shortcuts import get_object_or_404
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
            # Check if the password is at least 6 characters long
            if len(request.data["password"]) < 6:
                return Response(
                    {
                        "error": "Password must be at least 6 characters long"
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            new_user = reg_serializer.save()
            if new_user:
                try:
                    # Attempt to obtain an access token
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
                    r.raise_for_status()  # Raise an error if not successful
                    return Response(
                        r.json(), status=status.HTTP_201_CREATED
                    )
                except requests.exceptions.RequestException as e:
                    return Response(
                        {
                            "error": f"External request error: {str(e)}"
                        },
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    )
                except ValueError as e:
                    return Response(
                        {"error": str(e)},
                        status=status.HTTP_400_BAD_REQUEST,
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
    - HTTP 403 (Forbidden): If unauth'd user tries to access user details.
    - HTTP 500 (Internal Server Error): For unexpected server errors.

    """

    queryset = Account.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get(self, request, *args, **kwargs):
        try:
            instance = get_object_or_404(Account, pk=kwargs["pk"])
            # Check if the requesting user is the owner
            if request.user != instance:
                raise PermissionDenied(
                    "You do not have permission to access this user's details."
                )
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        except Account.DoesNotExist:
            raise NotFound(
                "User not found"
            )  # Raise NotFound exception
        except PermissionDenied as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_403_FORBIDDEN,
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def update(self, request, *args, **kwargs):
        try:
            instance = get_object_or_404(Account, pk=kwargs["pk"])
            # Check if the requesting user is the owner
            if request.user != instance:
                raise PermissionDenied(
                    "You do not have permission to update this user's details."
                )
            serializer = self.get_serializer(
                instance, data=request.data, partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        except Account.DoesNotExist:
            raise NotFound("User not found")
        except PermissionDenied as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_403_FORBIDDEN
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
