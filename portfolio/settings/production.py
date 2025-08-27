# portfolio/settings/production.py

import os
from .base import *

# -------------------------------------------------------------------------
# SECURITY
# -------------------------------------------------------------------------

# Secret key must be set in the environment (PythonAnywhere Web tab or OS env)
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

# Never run with debug turned on in production!
DEBUG = False

# Hosts/domain names that are valid for this site
# Example: "benjakabula.pythonanywhere.com"
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', '').split(',')

# -------------------------------------------------------------------------
# DATABASE (override if you’re using a production database)
# -------------------------------------------------------------------------
# DATABASES = {
#     'default': {
#         'ENGINE':   'django.db.backends.postgresql',
#         'NAME':     os.environ['DB_NAME'],
#         'USER':     os.environ['DB_USER'],
#         'PASSWORD': os.environ['DB_PASSWORD'],
#         'HOST':     os.environ.get('DB_HOST', 'localhost'),
#         'PORT':     os.environ.get('DB_PORT', ''),
#     }
# }

# -------------------------------------------------------------------------
# STATIC & MEDIA
# -------------------------------------------------------------------------
# Use WhiteNoise for static file serving
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# (STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT all inherited from base.py)

# -------------------------------------------------------------------------
# YOUTUBE INTEGRATION
# -------------------------------------------------------------------------
YOUTUBE_API_KEY    = os.environ.get('YOUTUBE_API_KEY', '')
YOUTUBE_CHANNEL_ID = os.environ.get('YOUTUBE_CHANNEL_ID', '')

# -------------------------------------------------------------------------
# OPTIONAL: Additional production-only settings
# -------------------------------------------------------------------------
# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
# X_FRAME_OPTIONS = 'DENY'
