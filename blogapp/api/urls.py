
from django.urls import path
from .views import Registration , Bloglist,BlogDetails, CatagoryList,CatagoryDetails


urlpatterns = [
    
    path("register", Registration.as_view(), name="registration"),
    path("posts", Bloglist.as_view(), name="blogs-list"),
    path("posts/<int:pk>", BlogDetails.as_view(), name="blogs-detail"),
    path("catagories", CatagoryList.as_view(), name="catagory-list"),
    path("catagories/<int:pk>", CatagoryDetails.as_view(), name="catagory-detail")
]