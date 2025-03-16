from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.models import User

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
