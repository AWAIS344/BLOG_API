from rest_framework import generics, status
from django.conf import settings
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import RegistrationSerializer

# from django.contrib.auth.models import User

from django.contrib.auth import get_user_model

User = get_user_model() 
class Registration(generics.CreateAPIView):
    serializer_class=RegistrationSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]  # Allow unauthenticated users to register

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    