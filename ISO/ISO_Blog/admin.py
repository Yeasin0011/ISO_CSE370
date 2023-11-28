from django.contrib import admin

from .models import Post, Category , user_profile

# Register your models here.

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(user_profile)