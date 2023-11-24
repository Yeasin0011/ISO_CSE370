from django import forms

from .models import Post, Category

choices = Category.objects.all().values_list('name','name')
choice_list= []
for item in choices:
    choice_list.append(item)
class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title', 'title_tag', 'author', 'category' , 'body')

        widgets={
            'title':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tell a interesting story'}),
            'title_tag':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apply a meaningful tag'}), 
            'author':forms.Select(attrs={'class': 'form-control', }),
            'category': forms.Select(choices=choice_list,attrs={'class': 'form-control', }),
            'body':forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Open your heart out!'}), 

        }

class EditForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title', 'title_tag', 'body')

        widgets={
            'title':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name a Interesting Title!'}), 
            'title_tag':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apply a meaningful tag'}), 
            'body':forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Open your heart out!'}), 

        }