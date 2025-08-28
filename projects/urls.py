# projects/urls.py

from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.project_list, name='project_list'),
    path('projects/add/', views.add_project, name='add_project'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),

    # YouTube‐feed standalone view (optional)
    path('youtube-feed/', views.youtube_feed, name='youtube_feed'),

    path('contact/', views.contact, name='contact'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),

    # robots.txt
    path(
        'robots.txt',
        TemplateView.as_view(template_name='robots.txt',
                             content_type='text/plain'),
        name='robots_txt',
    ),
]
