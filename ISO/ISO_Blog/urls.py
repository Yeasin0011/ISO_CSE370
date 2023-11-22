from django.urls import path
# from . import views 
from .views import Homeview, postDetailview,postAddview



urlpatterns = [
    # path('', views.home, name='home'),
    path('', Homeview.as_view(), name='Home'), 
    path('post/<int:pk>', postDetailview.as_view(), name="post_details"),
    path('add_post/', postAddview.as_view(), name='add_post')
]
