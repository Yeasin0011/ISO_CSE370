from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView 

from .models import Post

from .form import PostForm
# Create your views here.

# def home(request):
#     return render(request, 'home.html', {})

class Homeview(ListView):
    model=Post
    template_name='home.html'

class postDetailview(DetailView):
    model=Post
    template_name='post.details.html'

class postAddview(CreateView):
    model=Post
    form_class=PostForm
    template_name='post_add.html'
    # fields=('__all__')
    # fields=('Title', 'Body')