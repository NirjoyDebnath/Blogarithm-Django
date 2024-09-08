from rest_framework import serializers
from .models import Auth
from users.serializers import UserSerializer
from users.models import User

class AuthSerializer(serializers.ModelSerializer):
    username = serializers.CharField(min_length=3, max_length=50)
    password = serializers.CharField(min_length=3, max_length=50)
    class Meta:
        model = Auth
        fields = '__all__'


class AuthandUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(min_length=3, max_length=50)
    password = serializers.CharField(min_length=3, max_length=50)
    email = serializers.EmailField(
        error_messages={
            'invalid': 'Email must be a valid email address',
            'required': 'Email is required'
        }
    )
    name = serializers.CharField(min_length=3, max_length=50)
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user_data = {
            "username": validated_data.get("username"),
            "email": validated_data.get("email"),
            "name": validated_data.get("name")
        }

        user = User.objects.create(**user_data)
        print("User------->", user.id)
        auth_data = {
            "user_id": user,
            "username": validated_data.get("username"),
            "password": validated_data.get("password")
        }
        print(auth_data)
        Auth.objects.create(**auth_data)

        return validated_data

            # Handle the case where user_data is not present or valid
        raise ValueError("Invalid user data provided.")



