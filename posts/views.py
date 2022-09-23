from django.contrib.auth import get_user_model #new
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser #new
from .models import Post
from .permissions import IsAuthorOrReadonly #new
from .serializers import PostSerializer,UserSerializer

# Create your views here.
class PostViewset(viewsets.ModelViewSet):
    permission_classes=(IsAuthorOrReadonly,)  #new
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    
  
class UserViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAdminUser]#new
    queryset=get_user_model().objects.all()
    serializer_class=UserSerializer
    
    
