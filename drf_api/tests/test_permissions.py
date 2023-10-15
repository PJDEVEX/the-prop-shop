from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from accounts.models import Account
from drf_api.permissions import IsOwnerOrReadOnly


class IsOwnerOrReadOnlyTest(APITestCase):
    def setUp(self):
        # Create a user and a token for authentication
        self.user = Account.objects.create_user(
            email="testuser@example.com",
            username="testuser",
            first_name="Test",
            password="testpassword"
        )
        self.token, _ = Token.objects.get_or_create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

        # Create an instance that another user owns
        self.other_user = Account.objects.create_user(
            email="otheruser@example.com",
            username="otheruser",
            first_name="Other",
            password="otherpassword"
        )
