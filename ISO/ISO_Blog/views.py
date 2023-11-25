from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post, Category

from .form import PostForm, EditForm

from django.urls import reverse_lazy


class Homeview(ListView):
    model=Post
    template_name='home.html'
    ordering=['-post_date']
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(Homeview, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context



def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list': cat_menu_list})



def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'categories.html', {'cats': cats.title().replace('-', ' '), 'category_posts':category_posts})


class postDetailview(DetailView):
    model=Post
    template_name='post.details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(postDetailview, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context    

class postAddview(CreateView):
    model=Post
    form_class=PostForm
    template_name='post_add.html'
    # fields=('__all__')
    # fields=('Title', 'Body')
class categoryAddview(CreateView):
    model= Category
    #form_class=PostForm
    template_name='category_add.html'
    fields='__all__'
    # fields=('Title', 'Body')

class postUpdateview(UpdateView):
    model=Post
    form_class=EditForm
    template_name='update_post.html'

class postDeleteview(DeleteView):
    model=Post
    template_name='delete_post.html'
    success_url=reverse_lazy('Home')
   