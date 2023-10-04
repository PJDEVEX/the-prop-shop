from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

User = get_user_model()

class SignupViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.signup_url = reverse('signup')  # Replace with your actual URL name for the signup view

    def test_successful_signup(self):
        data = {
            "name": "Test User",
            "email": "test@example.com",
            "password": "Test123@",
            "password2": "Test123@",
        }

        response = self.client.post(self.signup_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("success", response.data)

        user_exists = User.objects.filter(email=data["email"]).exists()
        self.assertTrue(user_exists)

    def test_signup_with_existing_email(self):
        existing_user = User.objects.create_user(
            email="existing@example.com",
            password="Existing123@",
            name="Existing User",
        )

        data = {
            "name": "Test User",
            "email": "existing@example.com",
            "password": "Test123@",
            "password2": "Test123@",
        }

        response = self.client.post(self.signup_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("error", response.data)
        self.assertIn("Email already exists", response.data["error"])

    def test_signup_with_invalid_password(self):
        data = {
            "name": "Test User",
            "email": "test@example.com",
            "password": "invalid",
            "password2": "invalid",
        }

        response = self.client.post(self.signup_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("error", response.data)
        self.assertIn("Password must contain at least 6 characters", response.data["error"])

    def test_signup_with_non_matching_passwords(self):
        data = {
            "name": "Test User",
            "email": "test@example.com",
            "password": "Test123@",
            "password2": "Mismatch123@",
        }

        response = self.client.post(self.signup_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("error", response.data)
        self.assertIn("Passwords do not match", response.data["error"])
