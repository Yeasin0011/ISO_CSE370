from django.shortcuts import render , get_object_or_404

from django.views import generic

from django.views.generic import DetailView

from django.contrib.auth.forms import UserCreationForm

from django.urls import reverse_lazy

from .forms import SignUpForm, EditProfileForm

class PasswordsChangeView(PasswordChangeView):
    form_class= PasswordChangeForm
    success_url=reverse_lazy('home')




class UserRegistrationView(generic.CreateView):
    form_class=UserCreationForm
    template_name='registration/register.html'
    success_url=reverse_lazy('login')

    def get_object(self):
        return self.request.user