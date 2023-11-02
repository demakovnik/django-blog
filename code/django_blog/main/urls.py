
from django.urls import path

import main.views as main

app_name = 'main'

urlpatterns = [
    path('', main.index, name='index'),
    path('posts/', main.PostsList.as_view(), name='posts-index'),
    path('posts/<int:pk>/', main.PostDetailView.as_view(), name='post-detail'),
]
