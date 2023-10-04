from django.utils.safestring import mark_safe
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from django.contrib.auth import get_user_model
import re

User = get_user_model()


class SignupView(APIView):
    """
    API view for user registration and account creation.
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        """
        Handles POST requests for user registration.
        """
        data = self.request.data

        name = data["name"]
        email = data["email"]
        password = data["password"]
        password2 = data["password2"]

        # Password validation regex pattern
        password_pattern = (
            r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{6,}$"
        )

        if password == password2:
            if User.objects.filter(email=email).exists():
                error_message = "Email already exists"
                return Response({"error": error_message})
            else:
                if not re.match(password_pattern, password):
                    error_message = "Password must contain at least 6 characters, including at least one letter, one digit, and one special character (@$!%*#?&)."
                    return Response({"error": mark_safe(error_message)})
                else:
                    user = User.objects.create_user(
                        email=email, password=password, name=name
                    )

                    user.save()
                    return Response(
                        {"success": "Congratulations! User created successfully"}
                    )
        else:
            return Response({"error": "Passwords do not match"})
