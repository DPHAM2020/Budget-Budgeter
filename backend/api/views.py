from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()      # List of objects we are going to look at when creating a new user (prevents duplicate users)
    serializer_class = User            # Tells the view what kind of data we need to accept to make a new user
    permission_classes = [AllowAny]    # Allows anyone (even unauthenticated users) to create new accounts
