from django.urls import path, include
from post.views import *

urlpatterns = [
    path('list/', post_list, name='post_list'),
    path('detail/<int:pk>', post_detail, name='post_detail'),
    path('list_title/', post_title_list, name='post_title_list'),

]