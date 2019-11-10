"""URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

from apps.blog.views import ImageViewSet, PostViewSet, TagViewSet

router = routers.DefaultRouter()
router.register("tags", TagViewSet)
router.register("images", ImageViewSet)
router.register("posts", PostViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(router.urls)),
    path("api/v1/auth/", include("djoser.urls")),
    path("api/v1/auth/", include("djoser.urls.jwt")),
    path("api/v1/auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("health/", include("health_check.urls")),
    path("schema/", get_schema_view()),
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=settings.DEBUG))),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [
        path("docs/", include_docs_urls()),
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
    if "silk" in settings.INSTALLED_APPS:
        urlpatterns += [path("silk/", include("silk.urls", namespace="silk"))]
