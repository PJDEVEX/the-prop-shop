from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from .serializers import RegistrationSerializer, UsersSerializer
from .models import Account
from django.urls import reverse
import requests


class CreateAccount(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        reg_serializer = RegistrationSerializer(data=request.data)
        if reg_serializer.is_valid():
            new_user = reg_serializer.save()
            if new_user:
                base_url = request.build_absolute_uri('/')[:-1]
                token_url = f'{base_url}/api-auth/token'
                r = requests.post(token_url, data={
                    'username': new_user.email,
                    'password': request.data['password'],
                    'client_id': 'Your Client ID',
                    'client_secret': 'Your Client Secret',
                    'grant_type': 'password'
                })
                return Response(status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AllUsers(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Account.objects.all()
    serializer_class = UsersSerializer


class CurrentUser(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        serializer = UsersSerializer(self.request.user)
        return Response(serializer.data)
