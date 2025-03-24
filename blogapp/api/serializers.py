from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.models import User 
from blogapp.models import POSTS, Catagory

User = get_user_model()

class RegistrationSerializer(serializers.ModelSerializer):



    class Meta:
        model =User
        fields=['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user 

class CatagorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Catagory

        fields ="__all__"
    
    def validate(self,data):

        if data["name"] == data["description"]:
            raise serializers.ValidationError(["name and description should not be the same."])
        
        return data
    

class PostSerializer(serializers.ModelSerializer):

    author = serializers.CharField(source='author.username',read_only=True)
    catagory=serializers.CharField(source="catagory.name", read_only=True)
    class Meta:
        model = POSTS

        fields ="__all__"


    # def create(self, validated_data):
    #     """
    #     Assign the currently logged-in user as the author.
    #     """
    #     request = self.context.get('request')  # Get the request object
    #     if request and request.user.is_authenticated:
    #         validated_data['author'] = request.user  # Set the author automatically
    #     else:
    #         raise serializers.ValidationError({"author": "Authentication is required to create a post."})

    #     return POSTS.objects.create(**validated_data)

    def validate(self,data):

        if data["title"] == data["content"]:
            raise serializers.ValidationError(["Title and content should not be the same."])
        
        return data
    

