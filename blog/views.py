from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import  status
from rest_framework import permissions,generics
from blog.models import Blog
from django.contrib.auth import login
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from blog.serializers import RegisterSerializer,UserSerializer,LoginSerializer,BlogSerializer
from rest_framework.authtoken.serializers import AuthTokenSerializer



# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        
        })


class LoginAPI(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

#class LogoutApi(APIView):
  #  def get(self, request, format=None):
        # simply delete the token to force a login
      #  request.user.auth_token.delete()
       # return Response(status=status.HTTP_200_OK)


class BlogListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the Blog items for given requested user
        '''
        blogs = Blog.objects.filter(user = request.user.id)
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the blog with given blog data
        '''
        data = {
            'title': request.data.get('title'), 
            'content': request.data.get('content'), 
            'author': request.data.get('author'),
            'status':request.data.get('status') ,
            'user': request.user.id
        }
        serializer = BlogSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class BlogDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, blog_id, user_id):
        '''
        Helper method to get the object with given blog_id, and user_id
        '''
        try:
            return Blog.objects.get(id=blog_id, user = user_id)
        except Blog.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, blog_id, *args, **kwargs):
       
        blog_instance = self.get_object(blog_id, request.user.id)
        if not blog_instance:
            return Response(
                {"res": "Object with blog id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = BlogSerializer(blog_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)




    # 4. Update
    def put(self, request, blog_id, *args, **kwargs):
        '''
        Updates the blog item with given blog_id if exists
        '''
        blog_instance = self.get_object(blog_id, request.user.id)
        if not blog_instance:
            return Response(
                {"res": "Object with blog id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )

            
        data = {
            'title': request.data.get('title'), 
            'content': request.data.get('content'), 
            'author': request.data.get('author'),
            'status':request.data.get('status') ,
            'user': request.user.id
        }
        serializer = BlogSerializer(instance = blog_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, blog_id, *args, **kwargs):
        '''
        Deletes the blog item with given blog_id if exists
        '''
        blog_instance = self.get_object(blog_id, request.user.id)
        if not blog_instance:
            return Response(
                {"res": "Object with blog id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        blog_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK)


class BlogAllDetails(APIView):
    def get(self, request, format=None):
        all_blogs = Blog.objects.all()
        serializer = BlogSerializer(all_blogs, many=True)
        return Response(serializer.data) 

 #See all the users 

class UsersAllDetails(APIView):
    def get (self,request):
        all_user=User.objects.all()
        serializer=UserSerializer(all_user,many=True)
        return Response(serializer.data) 
        
 




