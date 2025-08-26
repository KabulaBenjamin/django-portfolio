from django.db import models
from django.utils.text import slugify
import datetime

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('web', 'Software & Web Development'),
        ('data', 'Data & Social Impact'),
    ]

    title           = models.CharField(max_length=200)
    slug            = models.SlugField(unique=True, blank=True)
    description     = models.TextField()
    category        = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    technologies    = models.CharField(max_length=200, blank=True, default='')
    github_link     = models.URLField(blank=True)
    live_demo       = models.URLField(blank=True)
    date_completed  = models.DateField(default=datetime.date.today)

    def save(self, *args, **kwargs):
        # Auto-generate slug from title if not set
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='images'
    )
    image   = models.ImageField(upload_to='projects/images/')

    def __str__(self):
        return f"{self.project.title} – Image"


class ProjectVideo(models.Model):
    project     = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='videos'
    )
    video       = models.FileField(
        upload_to='projects/videos/',
        blank=True,
        null=True
    )
    youtube_url = models.URLField(
        blank=True,
        null=True,
        help_text='Full YouTube URL (e.g. https://youtu.be/VIDEO_ID)'
    )

    def __str__(self):
        return f"{self.project.title} – Video"


class YouTubeVideo(models.Model):
    """
    Caches metadata for a channel’s latest videos via YouTube Data API
    """
    video_id     = models.CharField(max_length=20, unique=True)
    title        = models.CharField(max_length=200)
    published_at = models.DateTimeField()
    thumbnail    = models.URLField()

    def __str__(self):
        return self.title