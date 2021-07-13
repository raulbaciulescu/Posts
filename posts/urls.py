from django.conf import settings
from django.template.context_processors import static
from django.urls import path, include

from posts.views import PostList, PostCreate, PostDetail

app_name = 'posts'
urlpatterns = [
    path('', PostList.as_view(), name='list'),
    path('new/', PostCreate.as_view(), name='new'),
    path('posts/<pk>/', PostDetail.as_view(), name='detail'),
]