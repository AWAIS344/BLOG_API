from rest_framework import generics, status
from django.conf import settings
from blogapp.models import POSTS , Catagory
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import RegistrationSerializer , PostSerializer

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
    

class Bloglist(generics.ListCreateAPIView):
    
    serializer_class=PostSerializer
    queryset = POSTS.objects.all()
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            # Extract non_field_errors and return as a list
            return Response(serializer.errors.get("non_field_errors", serializer.errors), status=status.HTTP_400_BAD_REQUEST)
        
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    
    