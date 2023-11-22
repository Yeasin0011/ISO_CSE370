from django.shortcuts import render

from django.views.generic import ListView, DetailView 

from .models import Post
# Create your views here.

# def home(request):
#     return render(request, 'home.html', {})

class Homeview(ListView):
    model=Post
    template_name='home.html'

class postDetailview(DetailView):
    model=Post
    template_name='post.details.html'
