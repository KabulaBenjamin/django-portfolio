import os
from pathlib import Path

# -----------------------------------------------------------------------------
# BASE & ROOT DIRECTORIES
# -----------------------------------------------------------------------------
BASE_DIR  = Path(__file__).resolve().parent.parent
REPO_ROOT = BASE_DIR.parent

# -----------------------------------------------------------------------------
# ENV LOADING & SECURITY
# -----------------------------------------------------------------------------
env_file = REPO_ROOT / '.env'

if env_file.exists():
    # LOCAL DEVELOPMENT: Read from .env file
    from decouple import Config, RepositoryEnv, Csv
    config = Config(RepositoryEnv(env_file))
    
    SECRET_KEY         = config('DJANGO_SECRET_KEY', default='unsafe-secret-key')
    DEBUG              = config('DJANGO_DEBUG', default=True, cast=bool)
    ALLOWED_HOSTS      = config('DJANGO_ALLOWED_HOSTS', default='localhost,127.0.0.1', cast=Csv())
    YOUTUBE_API_KEY    = config('YOUTUBE_API_KEY', default='')
    YOUTUBE_CHANNEL_ID = config('YOUTUBE_CHANNEL_ID', default='')
else:
    # PRODUCTION (PythonAnywhere): Read from Environment Variables
    SECRET_KEY         = os.environ.get('DJANGO_SECRET_KEY', 'unsafe-secret-key')
    # Convert string 'True'/'False' to actual Boolean
    DEBUG              = os.environ.get('DJANGO_DEBUG', 'False') == 'True'
    # Split the comma-separated string into a list
    ALLOWED_HOSTS      = os.environ.get("DJANGO_ALLOWED_HOSTS", "benjakabula.pythonanywhere.com").split(",")
    YOUTUBE_API_KEY    = os.environ.get('YOUTUBE_API_KEY', '')
    YOUTUBE_CHANNEL_ID = os.environ.get('YOUTUBE_CHANNEL_ID', '')

# -----------------------------------------------------------------------------
# INSTALLED APPS
# -----------------------------------------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Your apps
    'projects.apps.ProjectsConfig',

    # Site framework & sitemaps
    'django.contrib.sites',
    'django.contrib.sitemaps',
]

SITE_ID = 1

# -----------------------------------------------------------------------------
# MIDDLEWARE
# -----------------------------------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Vital for production static files
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portfolio.urls'

# -----------------------------------------------------------------------------
# TEMPLATES
# -----------------------------------------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR  / 'templates',
            REPO_ROOT / 'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.static',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'portfolio.wsgi.application'

# -----------------------------------------------------------------------------
# DATABASE
# -----------------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':   BASE_DIR / 'db.sqlite3',
    }
}

# -----------------------------------------------------------------------------
# STATIC FILES (CSS, JS, images)
# -----------------------------------------------------------------------------
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    REPO_ROOT / 'static',
]

STATIC_ROOT = BASE_DIR / 'staticfiles'

# WhiteNoise storage for efficient serving
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# -----------------------------------------------------------------------------
# MEDIA FILES
# -----------------------------------------------------------------------------
MEDIA_URL  = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
