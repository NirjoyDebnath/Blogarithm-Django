from datetime import datetime

from django.core.serializers import serialize
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import Users


# Create your views here.
@api_view(['POST'])
def sign_up(request):
    print(request.data)
    serializer = UserSerializer(data = request.data)
    # return Response(request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(request.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_users(request):
    all_users = Users.objects.all()
    serializer = UserSerializer(all_users, many=True)
    serialized_data = serializer.data
    print(serialized_data)
    return Response(serialized_data)


