from django.shortcuts import render
from rest_framework import generics
from .models import Post
from .permissions import IsAuthorOrReadonly #new
from .serializers import PostSerializer

# Create your views here.
class PostList(generics.ListCreateAPIView):
    permission_classes=(IsAuthorOrReadonly,)  #new
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthorOrReadonly,) #new
    queryset=Post.objects.all()
    serializer_class=PostSerializer
