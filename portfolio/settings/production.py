# portfolio/settings/production.py

import os
from .base import *

# SECURITY
# Pull your SECRET_KEY from the WSGI env var we set
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
DEBUG = False

# Allow PythonAnywhere subdomain and any custom domains you add
ALLOWED_HOSTS = [
    'benjakabula.pythonanywhere.com',
    # 'www.kabulabenjamin.dev',
    # 'kabulabenjamin.dev',
]

# DATABASE
# Using SQLite on PythonAnywhere; adjust if you switch to Postgres
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# STATIC & MEDIA
# collectstatic will dump here; PythonAnywhere will serve /static/ from this folder
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# If you’re using django-whitenoise, uncomment this
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# MIDDLEWARE tweak if using Whitenoise (insert near top, just after SecurityMiddleware)
# MIDDLEWARE.insert(
#     MIDDLEWARE.index('django.middleware.security.SecurityMiddleware') + 1,
#     'whitenoise.middleware.WhiteNoiseMiddleware'
# )

# EMAIL (customize SMTP host/creds via env vars if you send mail)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'no-reply@benjakabula.pythonanywhere.com'
EMAIL_HOST = os.environ.get('EMAIL_HOST', '')
EMAIL_PORT = os.environ.get('EMAIL_PORT', '')
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', 'True') == 'True'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')

# YOUTUBE INTEGRATION
YOUTUBE_API_KEY = os.environ['YOUTUBE_API_KEY']
YOUTUBE_CHANNEL_ID = os.environ['YOUTUBE_CHANNEL_ID']

# Any additional production tweaks go here...