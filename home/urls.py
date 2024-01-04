from django.urls import path
from .views import (
    IndexView, PostsView, PostDetailView, TagView
)


app_name = 'home'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('posts', PostsView.as_view(), name='posts'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('post/tag/<tag>', TagView.as_view(), name='post_tags'),
]
