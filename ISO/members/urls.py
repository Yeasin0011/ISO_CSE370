from django.urls import path

from .views import UserRegistrationView , ShowProfilePageView



urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name="register"), 
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show_profilepage'),
]
