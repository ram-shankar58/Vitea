from django.contrib import admin
from django.urls import path, include
from notice.views import NoticeCreateAPIView, NoticeRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('login.urls')),
    path('notice/create/', NoticeCreateAPIView.as_view(), name='notice_create'),
    path('notice/<int:pk>/', NoticeRetrieveUpdateDestroyAPIView.as_view(), name='notice_retrieve_update_destroy'),
]
