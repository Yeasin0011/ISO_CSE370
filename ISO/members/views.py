from django.shortcuts import render , get_object_or_404 , PasswordChangeView

from django.views import generic

from django.views.generic import DetailView

from django.contrib.auth.forms import UserCreationForm

from django.urls import reverse_lazy

from django.forms import SignUpForm, EditProfileForm , PasswordChangeForm

class PasswordsChangeView(PasswordChangeView):
    form_class= PasswordChangeForm
    success_url=reverse_lazy('home')



from ISO_Blog.models import Profile


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'
    def get_context_data(self, *args, **kwargs):
        cat_menu = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)

        page_user = get_object_or_404(Profile, id = self.kwargs['pk'])

        context["page_user"] = page_user
        return context
    



class UserRegistrationView(generic.CreateView):
    form_class=UserCreationForm
    template_name='registration/register.html'
    success_url=reverse_lazy('login')

    def get_object(self):
        return self.request.user