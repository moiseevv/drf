from django.urls import path, include
from post.views import *

urlpatterns = [
    path('list/', post_list, name='post_list'),

]