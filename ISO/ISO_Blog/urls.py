from django.urls import path
# from . import views 
from .views import Homeview, postDetailview



urlpatterns = [
    # path('', views.home, name='home'),
    path('', Homeview.as_view(), name='Home'), 
    path('post/<int:pk>', postDetailview.as_view(), name="post_details")

]
