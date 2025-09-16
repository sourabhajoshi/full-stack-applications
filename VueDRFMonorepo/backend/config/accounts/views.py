# accounts/views.py
from rest_framework import viewsets
from .models import User, Profile, Role
from .serializers import UserSerializer, ProfileSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny


# ViewSet automatically gives list, create, retrieve, update, delete
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()  # DB query all users : Defines which DB rows this API can access.
    serializer_class = UserSerializer # Defines how rows → JSON and JSON → rows
    permission_classes = [AllowAny]  # anyone can register : Public endpoint
