from rest_framework import generics
from django.conf import settings
from .serializers import RegistrationSerializer
# from django.contrib.auth.models import User

from django.contrib.auth import get_user_model

User = get_user_model() 
class Registration(generics.CreateAPIView):
    serializer_class=RegistrationSerializer
    queryset = User.objects.all()