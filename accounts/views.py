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
    """

    permission_classes = [permissions.AllowAny]

    def post(self, request):
        """
        Create a new user account.
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
    """

    permission_classes = [permissions.AllowAny]
    queryset = Account.objects.all()
    serializer_class = UsersSerializer


class CurrentUser(APIView):
    """
    API endpoint to retrieve infor about the currently authenticated user.
    """

    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        """
        Retrieve user information for the currently authenticated user.
        """
        serializer = UsersSerializer(
            self.request.user, context={"request": request}
        )
        return Response(serializer.data)


class UserDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve and update the details of the account if you are the owner.
    """

    queryset = Account.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]
