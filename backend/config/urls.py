from django.conf import settings
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.urls import re_path
from django.views.generic import TemplateView
from django.views.static import serve as static_serve


urlpatterns = [
    path("django-admin/", admin.site.urls),

    path("api/accounts/", include("accounts.urls")),
    path("api/documents/", include("documents.urls")),
    path("api/templates/", include("templates_app.urls")),

    re_path(
        r"^media/(?P<path>.*)$",
        static_serve,
        {
            "document_root": settings.MEDIA_ROOT,
        },
    ),

    re_path(
        r"^(?!api/|django-admin/|static/|media/).*$",
        TemplateView.as_view(template_name="index.html"),
    ),
]