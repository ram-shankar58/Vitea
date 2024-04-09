from django.urls import path
from .views import *

urlpatterns = [
    path('create/', CreatePostView.as_view(), name='create_post'),
    path('get/', PostDetailView.as_view(), name='post_detail'),
    path('update/', PostDetailView.as_view(), name='post_update'),
]