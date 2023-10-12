from rest_framework import serializers
from .models import Account


class UsersSerializer(serializers.ModelSerializer):
    is_current_user = serializers.SerializerMethodField()

    def get_is_current_user(self, obj):
        """
        Check if the current user is the same as the serialized user
        """
        request = self.context["request"]
        return request.user == obj

    class Meta:
        model = Account
        fields = (
            "email",
            "username",
            "first_name",
            "last_name",
            "created_at",
            "updated_at",
            "image",
            "is_current_user",
        )


class RegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.
    """

    class Meta:
        model = Account
        fields = ("email", "username", "password", "first_name")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        """
        Create and return a new user instance after validating data.
        """
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class UserDetailSerializer(serializers.ModelSerializer):
    """
    Retrieving detailed user information.
    """

    class Meta:
        model = Account
        fields = (
            "email",
            "username",
            "first_name",
            "last_name",
            "created_at",
            "updated_at",
            "image",
        )
