# this is where the urls of our api/app will be stored
from django.urls import path
from profiles_api import views  

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
]