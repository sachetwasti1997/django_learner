from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.Serializer):
  class Meta:
    model = Post
    fields = ('id', 'title', 'author', 'excerpt', 'content', 'status')