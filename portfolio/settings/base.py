import os
from pathlib import Path
from decouple import Config, RepositoryEnv, Csv

# -----------------------------------------------------------------------------
# BASE & ROOT DIRECTORIES
# -----------------------------------------------------------------------------
# BASE_DIR points at portfolio/, REPO_ROOT at your repo’s root (where .env & manage.py live)
BASE_DIR  = Path(__file__).resolve().parent.parent
REPO_ROOT = BASE_DIR.parent

# -----------------------------------------------------------------------------
# ENV LOADING
# -----------------------------------------------------------------------------
# Tell python-decouple exactly where to find your .env
env_file = REPO_ROOT / '.env'
config   = Config(RepositoryEnv(env_file))

# -----------------------------------------------------------------------------
# SECURITY & DEBUG
# -----------------------------------------------------------------------------
SECRET_KEY   = config('DJANGO_SECRET_KEY', default='',       cast=str)
DEBUG        = config('DJANGO_DEBUG',      default=False,    cast=bool)
ALLOWED_HOSTS = config(
    'DJANGO_ALLOWED_HOSTS',
    default='localhost,127.0.0.1',
    cast=Csv()
)

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
    # whitenoise (if installed) will only run when DEBUG=False
    'whitenoise.middleware.WhiteNoiseMiddleware',
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
        'ENGINE':   'django.db.backends.sqlite3',
        'NAME':     BASE_DIR / 'db.sqlite3',
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
# STATIC FILES
# -----------------------------------------------------------------------------
STATIC_URL          = '/static/'
STATICFILES_DIRS    = [BASE_DIR / 'static']
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
YOUTUBE_API_KEY    = config('YOUTUBE_API_KEY',    default='', cast=str)
YOUTUBE_CHANNEL_ID = config('YOUTUBE_CHANNEL_ID', default='', cast=str)