from django.db import models

from django.conf import settings
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Profile(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    Country = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.username

class Catagory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.name
 
class POSTS(models.Model):

    title = models.CharField(max_length=10)
    content=models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status=models.CharField(max_length=20 , choices=[("Draft","Draft",("Published","Published"))], default="Draft")
    approved=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
