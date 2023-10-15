from django.test import TestCase
import responses
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework.request import Request
from ..models import Account
from ..serializers import UsersSerializer, UserDetailSerializer


class AccountViewsTest(APITestCase):
    def test_get_current_user(self):
        self.user = Account.objects.create_user(
            email="adam@example.com",
            username="adam",
            password="password123",
            first_name="Adam",
            last_name="Smith",
        )
        self.client.force_authenticate(user=self.user)
        url = reverse("users:current_user")
        response = self.client.get(url)

        # Create a request object manually
        request = Request(response.wsgi_request)

        # Provide the context with the request to the serializer
        serializer = UsersSerializer(
            self.user, context={"request": request}
        )

        # Test if the serialized data matches the response data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    @responses.activate
    def test_create_user_account(self):
        data = {
            "email": "newuser@example.com",
            "username": "newuser",
            "password": "password123",
            "first_name": "New",
            "last_name": "User",
        }
        url = reverse("users:create_user")

        # Mock the external request to prevent actual external requests
        responses.add(
            responses.POST,
            "https://8000-pjdevex-thepropshop-fhncw5hdrsb.ws-eu105.gitpod.io/api-auth/token",
            json={"access_token": "your_access_token"},
            status=200,
        )

        response = self.client.post(url, data)

        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertTrue(
            Account.objects.filter(username="newuser").exists()
        )

    def test_create_user_with_existing_email(self):
        # Create a user with a specific email
        existing_user = Account.objects.create_user(
            email="existing@example.com",
            username="existinguser",
            password="password123",
            first_name="Existing",
            last_name="User",
        )

        data = {
            # Use the same email as the existing user
            "email": "existing@example.com",
            "username": "newuser",
            "password": "password456",
            "first_name": "New",
            "last_name": "User",
        }

        url = reverse("users:create_user")
        response = self.client.post(url, data)

        self.assertEqual(
            response.status_code, status.HTTP_400_BAD_REQUEST
        )
        self.assertFalse(
            Account.objects.filter(username="newuser").exists()
        )

    def test_failed_user_registration(self):
        data = {
            "email": "invalid-email",  # Invalid email
            "password": "password123",
        }
        url = reverse("users:create_user")

        response = self.client.post(url, data)

        self.assertEqual(
            response.status_code, status.HTTP_400_BAD_REQUEST
        )
        self.assertFalse(
            Account.objects.filter(email="invalid-email").exists()
        )

    @responses.activate
    def test_successful_user_registration(self):
        data = {
            "email": "newuser@example.com",
            "username": "newuser",
            "password": "password123",
            "first_name": "New",
            "last_name": "User",
        }
        url = reverse("users:create_user")

        # Mock the external request to return a JSON response
        responses.add(
            responses.POST,
            "https://8000-pjdevex-thepropshop-fhncw5hdrsb.ws-eu105.gitpod.io/api-auth/token",
            json={"access_token": "your_access_token"},
            status=200,
        )

        response = self.client.post(url, data)

        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertTrue(
            Account.objects.filter(username="newuser").exists()
        )

    @responses.activate
    def test_user_registration_with_short_password(self):
        data = {
            "email": "shortpassword@example.com",
            "username": "shortuser",
            "password": "123",  # Password is too short
            "first_name": "Short",
            "last_name": "User",
        }
        url = reverse("users:create_user")

        # Mock the external request to return valid JSON
        responses.add(
            responses.POST,
            "https://8000-pjdevex-thepropshop-fhncw5hdrsb.ws-eu105.gitpod.io/api-auth/token",
            json={
                "access_token": "your_access_token"
            },  # Change this to valid JSON
            status=200,
        )

        response = self.client.post(url, data)

        self.assertEqual(
            response.status_code, status.HTTP_400_BAD_REQUEST
        )
        self.assertFalse(
            Account.objects.filter(username="shortuser").exists()
        )

    def test_get_full_name(self):
        user = Account(
            first_name="John",
            last_name="Doe",
        )
        self.assertEqual(user.get_full_name(), "John Doe")

    def test_get_short_name(self):
        user = Account(
            first_name="John",
            last_name="Doe",
        )
        self.assertEqual(user.get_short_name(), "John")


class UserDetailTest(APITestCase):
    def setUp(self):
        # Create a user for testing
        self.user = Account.objects.create_user(
            email="testuser@example.com",
            username="testuser",
            password="password123",
            first_name="Test",
            last_name="User",
        )
        self.url = reverse("users:user_detail", args=[self.user.id])
        self.client.force_authenticate(user=self.user)

    def test_get_user_detail(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Create a serializer for the user
        serializer = UserDetailSerializer(self.user)
        self.assertEqual(response.data, serializer.data)

    def test_update_user_detail(self):
        updated_data = {
            "username": "new_username",  # Update the username
            "password": "new_password",  # Update the password
            "first_name": "Updated",  # Update the first name
            "last_name": "Name",  # Update the last name
        }
        response = self.client.put(
            self.url, updated_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Refresh the user instance and check if it's updated
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, updated_data["username"])
        self.assertEqual(
            self.user.first_name, updated_data["first_name"]
        )
        self.assertEqual(
            self.user.last_name, updated_data["last_name"]
        )

    def test_update_other_user_detail(self):
        # Create another user for testing
        other_user = Account.objects.create_user(
            email="otheruser@example.com",
            username="otheruser",
            password="password123",
            first_name="Other",
            last_name="User",
        )

        # Attempt updating another user's account with test user's credentials.
        url = reverse("users:user_detail", args=[other_user.id])
        updated_data = {
            "username": "new_username",  # Update the username
            "password": "new_password",  # Update the password
            "first_name": "Updated",  # Update the first name
            "last_name": "Name",  # Update the last name
        }
        response = self.client.put(url, updated_data, format="json")

        # Test user shouldn't have permission to update other user's details
        self.assertEqual(
            response.status_code, status.HTTP_403_FORBIDDEN
        )
