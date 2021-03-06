# this is where the urls of our api/app will be stored
from django.urls import path, include
from profiles_api import views  
from rest_framework.routers import DefaultRouter

# mapping url to viewset is diff from mapping it to apiview
router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
]

# what do you determine what is an apiview or a viewset