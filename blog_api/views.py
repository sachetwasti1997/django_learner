from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer

# Create your views here.


@api_view(['GET'])
def getPostList(request):
  posts = Post.objects.all()
  serializer = PostSerializer(posts)
  return Response(serializer.data)

