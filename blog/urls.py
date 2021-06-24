from django.conf.urls import url
from django.urls import path, include
from .views import BlogListApiView, BlogDetailApiView,RegisterApi,BlogAllDetails

urlpatterns = [
    path('api/register/', RegisterApi.as_view(), name='register'),
    path('', BlogListApiView.as_view()),
    path('<int:blog_id>/', BlogDetailApiView.as_view()),
    path('all/blog/',BlogAllDetails.as_view())
]