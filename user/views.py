"""
Views for the API user
"""
from django.shortcuts import render

from rest_framework import generics
from user.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """Creating a new user in the system"""
    serializer_class = UserSerializer

