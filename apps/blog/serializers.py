from rest_framework import serializers

from apps.blog.models import Image, Post, Tag


class TagSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="tag-detail")

    class Meta:
        model = Tag
        fields = "__all__"
        read_only_fields = ("created_at", "updated_at")


class ImageSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="image-detail")

    class Meta:
        model = Image
        fields = "__all__"
        read_only_fields = ("created_at", "updated_at")


class PostSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="post-detail")
    tag_slugs = serializers.SlugRelatedField(
        write_only=True,
        source="tags",
        queryset=Tag.objects.all(),
        slug_field="name",
        many=True,
    )
    tags = TagSerializer(read_only=True, many=True)
    image_ids = serializers.PrimaryKeyRelatedField(
        write_only=True, source="images", queryset=Image.objects.all(), many=True
    )
    images = ImageSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "url",
            "title",
            "content",
            "draft",
            "tag_slugs",
            "tags",
            "image_ids",
            "images",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ("created_at", "updated_at")
