from rest_framework import serializers
from .models import Users
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(min_length=3, max_length=50)
    email = serializers.EmailField(
        error_messages={
            'invalid': 'Email must be a valid email address',
            'required': 'Email is required'
        }
    )
    name = serializers.CharField(min_length=3, max_length=50)
    class Meta:
        model = Users
        fields = ['name', 'email', 'username', 'password']

    def create(self, validated_data):
        user = Users.objects.create(email=validated_data['email'], name=validated_data['name'], username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(
        error_messages={
            'invalid': 'Email must be a valid email address',
            'required': 'Email is required'
        }
    )
    password = serializers.CharField(min_length=3, max_length=50)

    def validate(self, data):
        user = authenticate(email=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Invalid credentials')
        print(user, user.id)
        return user

class UpdateUserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(min_length=3, max_length=50)
    class Meta:
        model = Users
        fields = ['name']
