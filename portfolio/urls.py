# portfolio/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from pathlib import Path
from django.contrib.sitemaps.views import sitemap
from projects.sitemaps import StaticViewSitemap, ProjectSitemap, VideoSitemap

BASE_DIR = Path(__file__).resolve().parent.parent

# Define your sitemaps
sitemaps = {
    "static": StaticViewSitemap,
    "projects": ProjectSitemap,
    "videos": VideoSitemap,
}

# Core URL patterns
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("projects.urls")),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
]

# Serve media & static in DEBUG mode
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=BASE_DIR / "static",
    )