from rest_framework import generics, status
from django.conf import settings
from rest_framework import serializers
from blogapp.models import POSTS , Catagory
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import RegistrationSerializer , PostSerializer

# from django.contrib.auth.models import User

from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthorOrAdmin , IsAuth

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
    permission_classes=[IsAuthorOrAdmin, IsAuth]

    # def get_permissions(self):
    #     """
    #     Assign permissions based on the request method.
    #     """
    #     if self.request.method == "GET":
    #         return [IsAuthenticated()]  # Only authenticated users can view posts
    #     elif self.request.method == "POST":
    #         return [IsAuthorOrAdmin()]  # Only authors or admins can create posts
    #     return super().get_permissions()

    def perform_create(self, serializer):
        if not self.request.user.is_authenticated:
            raise serializers.ValidationError({"error": "Authentication required to create a post."})
        serializer.save(author=self.request.user)


class BlogDetails(generics.RetrieveUpdateDestroyAPIView):

    serializer_class=PostSerializer
    queryset = POSTS.objects.all()
    
    


    
    