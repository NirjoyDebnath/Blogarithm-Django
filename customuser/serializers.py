from rest_framework import serializers
from .models import Users

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
        fields = ['name', 'email', 'username']

    def create(self, validated_data):
        user = Users.objects.create(email=validated_data['email'], name=validated_data['name'], username=validated_data['username'])
        user.set_password(validated_data['name'])
        user.save()
        return user

