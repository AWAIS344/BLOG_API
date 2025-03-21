
from django.urls import path
from .views import Registration , Bloglist,BlogDetails


urlpatterns = [
    
    path("register", Registration.as_view(), name="registration"),
    path("posts", Bloglist.as_view(), name="blogs-list"),
    path("posts/<int:pk>", BlogDetails.as_view(), name="blogs-detail"),

]