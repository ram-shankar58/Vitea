from django.urls import path
from .views import *

urlpatterns = [
    path('create/', CreatePostView.as_view(), name='create_post'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('<int:pk>/comment/', CreateCommentView.as_view(), name='create_comment'),
    path('comment/<int:pk>/', CommentDetailView.as_view(), name='comment_detail'),
    path('comment/<int:pk>/reply/', CreateReplyView.as_view(), name='create_reply'),
    path('top/', TopPostsView.as_view(), name='top_posts'),
    path('board/', BoardPostsView.as_view(), name='board_posts'),
]