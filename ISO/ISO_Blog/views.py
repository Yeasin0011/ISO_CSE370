from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post

from .form import PostForm, EditForm

from django.urls import reverse_lazy


class Homeview(ListView):
    model=Post
    template_name='home.html'
    ordering=['-post_date']

class postDetailview(DetailView):
    model=Post
    template_name='post.details.html'

class postAddview(CreateView):
    model=Post
    form_class=PostForm
    template_name='post_add.html'
    # fields=('__all__')
    # fields=('Title', 'Body')


class postUpdateview(UpdateView):
    model=Post
    form_class=EditForm
    template_name='update_post.html'

class postDeleteview(DeleteView):
    model=Post
    template_name='delete_post.html'
    success_url=reverse_lazy('Home')
   