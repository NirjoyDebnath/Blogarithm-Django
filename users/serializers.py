from rest_framework import serializers
from .models import User

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
        model = User
        fields = '__all__'

