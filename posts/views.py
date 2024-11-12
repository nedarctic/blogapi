from rest_framework import generics

from .serializers import PostSerializer
from .models import Post

class ListPost(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class DetailPost(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
