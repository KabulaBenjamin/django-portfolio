# portfolio/settings/local.py

from .base import *

SECRET_KEY = 'nwvU0z9kZ8TjQvJl2hFcvROGebZdEF_H'
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Dev email backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# YouTube API keys (dev only)
YOUTUBE_API_KEY = 'AIzaSyB_DhP40WRHmPTJvzX6wHb9s3FRq8SF6JU'
YOUTUBE_CHANNEL_ID = 'UCDMhxpf1T3kqI5_evrYXUHg'