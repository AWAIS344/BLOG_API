from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.models import User 
from blogapp.models import POSTS

User = get_user_model()

class RegistrationSerializer(serializers.ModelSerializer):



    class Meta:
        model =User
        fields=['username', 'email', 'password']

        def create(self, validated_data):
            user = settings.AUTH_USER_MODEL.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        
            return user 


class PostSerializer(serializers.ModelSerializer):

    author = serializers.CharField(source='author.username')
    class Meta:
        model = POSTS

        fields ="__all__"

    def validate(self,data):

        if data["title"] == data["content"]:
            raise serializers.ValidationError(["Title and content should not be the same."])
        
        return data
    
