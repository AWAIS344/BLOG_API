from django.contrib import admin
from .models import POSTS, Profile, Catagory

# Register your models here.
admin.site.register(POSTS)
admin.site.register(Profile)
admin.site.register(Catagory)
