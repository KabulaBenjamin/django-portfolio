from django.contrib import admin
from .models import Project, ProjectImage, ProjectVideo

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

class ProjectVideoInline(admin.TabularInline):
    model = ProjectVideo
    fields = ['video', 'youtube_url']
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = (ProjectImageInline, ProjectVideoInline)
    list_display = ('title', 'category', 'date_completed')
    search_fields = ('title', 'technologies')
    list_filter = ('category', 'date_completed')

@admin.register(ProjectVideo)
class ProjectVideoAdmin(admin.ModelAdmin):
    list_display = ('project', 'youtube_url', 'video')
    search_fields = ('project__title',)
    list_filter = ('project',)