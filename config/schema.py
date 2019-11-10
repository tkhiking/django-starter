import graphene
from graphene_django.debug import DjangoDebug

import apps.blog.schema


class Query(apps.blog.schema.Query, graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name="__debug")


schema = graphene.Schema(query=Query)
