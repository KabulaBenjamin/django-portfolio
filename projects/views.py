# projects/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, ProjectImage, ProjectVideo, YouTubeVideo
from .forms import ProjectForm

# Reusable contact/social info
CONTACT_INFO = {
    'phone1': '+254787978403',
    'phone2': '+254798030091',
    'github': 'https://github.com/KabulaBenjamin',
    'linkedin': 'https://linkedin.com/in/koikoi-benjamin-2b9370162',
    'email': 'kabulabenjamin25@gmail.com',
    'twitter': 'https://twitter.com/koikoibenjamin',
    'facebook': 'https://facebook.com/koikoi.benjamin',
}


def home(request):
    """
    Single-page home: hero + project grid + YouTube feed + contact + privacy
    """
    projects = Project.objects.all()
    # fetch latest 5 videos
    youtube_videos = YouTubeVideo.objects.order_by('-published_at')[:5]
    print(f"DEBUG [home]: found {youtube_videos.count()} YouTube videos")

    context = {
        'projects': projects,
        'youtube_videos': youtube_videos,
        **CONTACT_INFO,
    }
    return render(request, 'projects/home.html', context)


def project_list(request):
    """Standalone projects list page."""
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {
        'projects': projects
    })


def project_detail(request, pk):
    """Detail page for a single project."""
    project = get_object_or_404(Project, pk=pk)
    images = project.images.all()
    videos = project.videos.all()
    return render(request, 'projects/project_detail.html', {
        'project': project,
        'images': images,
        'videos': videos
    })


def add_project(request):
    """Form to create a new project (with images/videos)."""
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save()
            for img in request.FILES.getlist('image'):
                ProjectImage.objects.create(project=project, image=img)
            for vid in request.FILES.getlist('video'):
                ProjectVideo.objects.create(project=project, video=vid)
            return redirect('home')
    else:
        form = ProjectForm()

    return render(request, 'projects/project_form.html', {
        'form': form
    })


def contact(request):
    """Contact page (or block on home)."""
    return render(request, 'projects/contact.html', CONTACT_INFO)


def privacy_policy(request):
    """Privacy policy page."""
    return render(request, 'projects/privacy.html')


def youtube_feed(request):
    """Standalone YouTube‐feed page (if you ever need it)."""
    youtube_videos = YouTubeVideo.objects.order_by('-published_at')[:5]
    print(f"DEBUG [youtube_feed]: found {youtube_videos.count()} YouTube videos")
    return render(request, 'projects/youtube_feed.html', {
        'youtube_videos': youtube_videos
    })
