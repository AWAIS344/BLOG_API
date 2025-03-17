
from django.urls import path
from .views import Registration , Bloglist


urlpatterns = [
    
    path("register", Registration.as_view(), name="registration"),
    path("posts", Bloglist.as_view(), name="blogs-list"),
]