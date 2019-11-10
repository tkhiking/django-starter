import graphene
from graphene_django.types import DjangoObjectType

from apps.blog.models import Image, Post, Tag


class TagType(DjangoObjectType):
    class Meta:
        model = Tag


class ImageType(DjangoObjectType):
    class Meta:
        model = Image


class PostType(DjangoObjectType):
    class Meta:
        model = Post


class Query(object):
    all_tags = graphene.List(TagType)
    all_images = graphene.List(ImageType)
    all_posts = graphene.List(PostType)

    def resolve_all_tags(self, info, **kwargs):
        return Tag.objects.all()

    def resolve_all_images(self, info, **kwargs):
        return Image.objects.all()

    def resolve_all_posts(self, info, **kwargs):
        return Post.objects.all().prefetch_related("tags").prefetch_related("images")
