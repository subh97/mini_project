
from django.urls import path
from blog.views import( 
    LoginAPI, BlogAllDetails,UsersAllDetails
    ,BlogListApiView,BlogDetailApiView,
    RegisterAPI)
from blog.views import LogoutApiView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/',LoginAPI.as_view(),name='login'),
    path('api/logout/',LogoutApiView.as_view(),name='logout'),
    path('blog/', BlogListApiView.as_view()),
    path('blog/<int:blog_id>/', BlogDetailApiView.as_view()),
    path('all/blog/',BlogAllDetails.as_view()),
    path('user/',UsersAllDetails.as_view()),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
"""  
    
    
    https://thinkster.io/tutorials/django-json-api/authentication
    
    https://medium.com/django-rest/logout-django-rest-framework-eb1b53ac6d35"""