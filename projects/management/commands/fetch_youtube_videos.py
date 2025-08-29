# projects/management/commands/sync_youtube.py

from django.core.management.base import BaseCommand
from django.conf import settings
from googleapiclient.discovery import build

from projects.models import YouTubeVideo

class Command(BaseCommand):
    help = 'Sync latest YouTube videos and remove any that have been deleted or made private'

    def handle(self, *args, **options):
        youtube = build('youtube', 'v3', developerKey=settings.YOUTUBE_API_KEY)

        # 1. Search for the latest video IDs on your channel
        search_response = youtube.search().list(
            part='id',
            channelId=settings.YOUTUBE_CHANNEL_ID,
            order='date',
            maxResults=10
        ).execute()

        # 2. Extract only the valid videoId strings
        video_ids = [
            item['id'].get('videoId')
            for item in search_response.get('items', [])
            if item['id'].get('videoId')
        ]
        if not video_ids:
            self.stdout.write('No video IDs found on channel.')
            return

        # 3. Fetch snippet details for those IDs (deleted/private videos won't return here)
        videos_response = youtube.videos().list(
            part='snippet',
            id=','.join(video_ids)
        ).execute()

        live_ids = {video['id'] for video in videos_response.get('items', [])}

        # 4. Purge any YouTubeVideo in DB whose video_id is not in the live set
        YouTubeVideo.objects.exclude(video_id__in=live_ids).delete()

        # 5. Upsert each live video’s metadata
        for video in videos_response.get('items', []):
            vid_id  = video['id']
            snippet = video['snippet']

            YouTubeVideo.objects.update_or_create(
                video_id=vid_id,
                defaults={
                    'title':        snippet['title'],
                    'published_at': snippet['publishedAt'],
                    'thumbnail':    snippet['thumbnails']['high']['url'],
                }
            )

        self.stdout.write(self.style.SUCCESS(
            f'Synced {len(live_ids)} videos and removed deleted ones.'
        ))