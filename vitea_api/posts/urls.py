from django.urls import path
from .views import *

urlpatterns = [
    path('create/', CreatePostView.as_view(), name='create_post'),
    path('<int:pk>/get/', PostDetailView.as_view(), name='post_detail'),
    path('<int:pk>/update/', PostDetailView.as_view(), name='post_update'),
]