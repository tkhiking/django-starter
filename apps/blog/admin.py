from django.contrib import admin

from apps.blog.models import Image, Post, Tag

admin.site.register(Tag)
admin.site.register(Image)
admin.site.register(Post)
