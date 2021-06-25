from django.conf.urls import url
from django.urls import path, include
from .views import BlogListApiView, BlogDetailApiView,RegisterApi,BlogAllDetails,UsersAllDetails

urlpatterns = [
    path('api/register/', RegisterApi.as_view(), name='register'),
    path('blog/', BlogListApiView.as_view()),
    path('blog/<int:blog_id>/', BlogDetailApiView.as_view()),
    path('all/blog/',BlogAllDetails.as_view()),
    path('user/',UsersAllDetails.as_view())
]