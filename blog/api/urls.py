from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
import os
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views
from blog.api.views import PostViewSet, UserDetail, TagViewSet

from rest_framework.routers import DefaultRouter


schema_view = get_schema_view(
    openapi.Info(
        title="Blango API",
        default_version="v1",
        description="API for Blango Blog",
    ),
    url=f"https://{os.environ.get('CODIO_HOSTNAME')}-8000.codio.io/api/v1/",
    public=True,
)

api_urlpatterns = [
    path("users/<str:email>", UserDetail.as_view(), name="api_user_detail"),

]

# important to format suffix before swagger part
# because it should be not formatted
api_urlpatterns = format_suffix_patterns(api_urlpatterns )

# instantiate the router and register the viewset for Tags
router = DefaultRouter()
# registering Tags will add /api/v1/tags
router.register("tags", TagViewSet)
# registering Posts will add /api/v1/posts
router.register("posts", PostViewSet)

urlpatterns = [
    path("auth/", include("rest_framework.urls")),
    path("token-auth/", views.obtain_auth_token),

    # Swagger routes (not wrapped in format_suffix_patterns)
    # Raw schema endpoints
    re_path(r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    # Interactive Swagger UI
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    # adding created router
    path("", include(router.urls)),
]

# Add the API routes last
urlpatterns += api_urlpatterns