from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.utils.translation import gettext_lazy as _


class CustomAccountManager(BaseUserManager):
    """
    Custom manager for the Account model.
    """

    def create_user(
        self, email, username, first_name, password, **other_fields
    ):
        """
        Create and return a regular user.
        """
        if not email:
            raise ValueError(_("Please provide an email address"))
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            first_name=first_name,
            **other_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(
        self, email, username, first_name, password, **other_fields
    ):
        """
        Create and return a superuser.
        """
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)
        if other_fields.get("is_staff") is not True:
            raise ValueError(
                _("Please assign is_staff=True for superuser")
            )
        if other_fields.get("is_superuser") is not True:
            raise ValueError(
                _("Please assign is_superuser=True for superuser")
            )
        return self.create_user(
            email, username, first_name, password, **other_fields
        )


class Account(AbstractBaseUser, PermissionsMixin):
    """
    Custom User Model representing an account with email as the username.
    """

    email = models.EmailField(unique=True)
    username = models.CharField(_("User Name"), max_length=150)
    first_name = models.CharField(_("First Name"), max_length=150)
    last_name = models.CharField(_("Last Name"), max_length=150)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name"]

    def __str__(self):
        """
        Return the email as the string representation of the user.
        """
        return self.email
