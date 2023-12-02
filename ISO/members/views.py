from django.shortcuts import render , get_object_or_404

from django.views import generic

from django.contrib.auth.forms import UserCreationForm

from django.urls import reverse_lazy


class UserRegistrationView(generic.CreateView):
    form_class=UserCreationForm
    template_name='registration/register.html'
    success_url=reverse_lazy('login')
