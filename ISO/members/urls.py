from django.urls import path

from .views import UserRegistrationView, UserEditView, PasswordsChangeView , ShowProfilePageView

from django.contrib.auth import views as auth_views



urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name="register"),
    path('edit_profile/', UserEditView.as_view(), name="edit_profile"),
    path('members/password/', PasswordsChangeView.as_view(template_name="registration/change-password.html")),
    # path('password/', auth_views.PasswordChangeView.as_view()),
    path("<int:pk>/profile", ShowProfilePageView.as_view(), name='show_profile_page'),

      
    
]
