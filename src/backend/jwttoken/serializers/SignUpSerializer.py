__doc__="""
sign up serializer

This file contains the SignUpSerializer class, which is used to serialize the data for a new user.

the return value of the create method is {id,email} of the user object that was created.
"""

from rest_framework import serializers
from django.contrib.auth import get_user_model


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("password", "email", "id")
        extra_kwargs = {"password": {"write_only": True}, "id": {"read_only": True}}

    def create(self, validated_data):
        validated_data["username"] = validated_data["email"]
        user = get_user_model().objects.create_user(**validated_data)
        return {"id": user.id, "email": user.email}
    
    def validate(self, attrs):
        email = attrs.get("email", "")
        if get_user_model().objects.filter(email=email).exists():
            raise serializers.ValidationError({"email": ("Email is already in use")})
        return super().validate(attrs)
    
    def validate_password(self, value: str) -> str:
        if len(value) < 8:
            raise serializers.ValidationError(
                "Password must be at least 8 characters long."
            )
        return value
    
    def validate_email(self, value: str) -> str:
        if not value:
            raise serializers.ValidationError("Email is required")
        return value
    
