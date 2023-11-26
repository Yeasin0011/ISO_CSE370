from django.shortcuts import render,get_object_or_404

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post, Category

from .form import PostForm, EditForm

from django.urls import reverse_lazy, reverse

from django.http import HttpResponseRedirect

#just regular functional view enough for that
def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse("post_details", args=[str(pk)]))

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

        stuff= get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
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
   