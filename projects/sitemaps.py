from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Project, ProjectVideo

class StaticViewSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return ["home", "project_list", "contact", "privacy_policy"]

    def location(self, item):
        return reverse(item)

class ProjectSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return Project.objects.all()

    def lastmod(self, obj):
        return obj.updated_at  # or obj.published_at

class VideoSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.6

    def items(self):
        return ProjectVideo.objects.all()

    def lastmod(self, obj):
        return obj.published_at