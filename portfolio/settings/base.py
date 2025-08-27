import os
from pathlib import Path
from decouple import Config, RepositoryEnv, Csv

# -----------------------------------------------------------------------------
# BASE & ROOT DIRECTORIES
# -----------------------------------------------------------------------------
BASE_DIR  = Path(__file__).resolve().parent.parent
REPO_ROOT = BASE_DIR.parent

# -----------------------------------------------------------------------------
# ENV LOADING
# -----------------------------------------------------------------------------
env_file = REPO_ROOT / '.env'
if env_file.exists():
    config = Config(RepositoryEnv(env_file))   # Local dev → read from .env
else:
    config = os.environ.__getitem__            # Production (PythonAnywhere)

# -----------------------------------------------------------------------------
# SECURITY & DEBUG
# -----------------------------------------------------------------------------
SECRET_KEY = config('DJANGO_SECRET_KEY', default='unsafe-secret-key')
DEBUG      = config('DJANGO_DEBUG', default=False, cast=bool) \
             if callable(getattr(config, "get", None)) else bool(os.environ.get("DJANGO_DEBUG", False))

# ALLOWED_HOSTS needs special handling for Csv() casting
if env_file.exists():
    ALLOWED_HOSTS = config('DJANGO_ALLOWED_HOSTS', default='localhost,127.0.0.1', cast=Csv())
else:
    ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "localhost,127.0.0.1").split(",")

# -----------------------------------------------------------------------------
# INSTALLED APPS
# -----------------------------------------------------------------------------
INSTALLED_APPS = [
    # Django core
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
    'whitenoise.middleware.WhiteNoiseMiddleware',  # only applies when DEBUG=False
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
# DATABASE (SQLite by default; override in production.py if needed)
# -----------------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':   BASE_DIR / 'db.sqlite3',
    }
}

# -----------------------------------------------------------------------------
# PASSWORD VALIDATION
# -----------------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# -----------------------------------------------------------------------------
# INTERNATIONALIZATION
# -----------------------------------------------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE     = 'UTC'
USE_I18N      = True
USE_TZ        = True

# -----------------------------------------------------------------------------
# STATIC FILES (CSS, JS, images)
# -----------------------------------------------------------------------------
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    REPO_ROOT / 'static',
]

STATIC_ROOT         = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# -----------------------------------------------------------------------------
# MEDIA FILES
# -----------------------------------------------------------------------------
MEDIA_URL  = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# -----------------------------------------------------------------------------
# DEFAULT AUTO FIELD
# -----------------------------------------------------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# -----------------------------------------------------------------------------
# YOUTUBE INTEGRATION
# -----------------------------------------------------------------------------
YOUTUBE_API_KEY    = config('YOUTUBE_API_KEY', default='')
YOUTUBE_CHANNEL_ID = config('YOUTUBE_CHANNEL_ID', default='')
