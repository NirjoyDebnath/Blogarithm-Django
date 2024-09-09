from datetime import datetime

from django.core.serializers import serialize
from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .permissions import IsSameUserOrReadOnly
from .serializers import UserSerializer, LoginSerializer, UpdateUserSerializer
from .models import Users
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.
@api_view(['POST'])
def sign_up(request):
    serializer = UserSerializer(data = request.data)
    # return Response(request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(request.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def log_in(request):
    email = request.data.get("email")
    password = request.data.get("password")

    serializer = LoginSerializer(data = {"email": email, "password": password})

    if serializer.is_valid():
        print("from views", serializer.data)
        user = Users.objects.get(email=email)
        refresh = RefreshToken.for_user(user)
        response = {"Message": "Log In successful", "access_token": str(refresh.access_token), "refresh_token": str(refresh)}
        return Response(response, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserList(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    queryset = Users.objects.all()

class User(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsSameUserOrReadOnly]
    serializer_class = UpdateUserSerializer
    queryset = Users.objects.all()



