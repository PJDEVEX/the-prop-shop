from django.test import TestCase
from accounts.models import Account, CustomAccountManager


class AccountModelTest(TestCase):
    def setUp(self):
        # Create a sample user account for testing
        self.user = Account.objects.create(
            email="testuser@example.com",
            username="testuser",
            first_name="Test",
            last_name="User",
        )

    def test_account_creation(self):
        """
        Test whether an account is created correctly.
        """
        self.assertEqual(self.user.email, "testuser@example.com")
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.first_name, "Test")
        self.assertEqual(self.user.last_name, "User")
        self.assertEqual(self.user.is_staff, False)
        self.assertEqual(self.user.is_active, True)

    def test_account_str_method(self):
        """
        Test the __str__ method of the Account model.
        """
        self.assertEqual(str(self.user), "testuser@example.com")

    def test_account_default_image(self):
        """
        Test the default image value for the account.
        """
        # Check if the image field defaults to the expected value
        self.assertEqual(
            self.user.image, "../default_profile_gj2yan.jpg"
        )

    def test_account_update(self):
        """
        Test updating user account information.
        """
        self.user.first_name = "Updated"
        self.user.last_name = "User"
        self.user.save()
        updated_user = Account.objects.get(pk=self.user.pk)
        self.assertEqual(updated_user.first_name, "Updated")

    def test_account_deactivation(self):
        """
        Test deactivating a user account.
        """
        self.user.is_active = False
        self.user.save()
        deactivated_user = Account.objects.get(pk=self.user.pk)
        self.assertFalse(deactivated_user.is_active)

    def test_account_staff_status(self):
        """
        Test changing the staff status of a user account.
        """
        self.user.is_staff = True
        self.user.save()
        staff_user = Account.objects.get(pk=self.user.pk)
        self.assertEqual(staff_user.is_staff, True)
