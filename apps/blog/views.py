from rest_framework import viewsets

from apps.blog.models import Image, Post, Tag
from apps.blog.serializers import ImageSerializer, PostSerializer, TagSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().prefetch_related("tags").prefetch_related("images")
    serializer_class = PostSerializer
