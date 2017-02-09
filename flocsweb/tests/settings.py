"""Django settings for testing
"""

import dj_database_url
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '34r0-rk47e3-ka+3d+@!@e+%a9qr##6duf0t(!#1sm$&zw&8!y'
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')


ON_STAGING = os.getenv('ON_STAGING', "False") == "True"
ON_PRODUCTION = os.getenv('ON_AL', "False") == "True" and not ON_STAGING
DEVELOPMENT = not ON_STAGING and not ON_PRODUCTION
DEBUG = (not ON_PRODUCTION) or (os.getenv('DJANGO_DEBUG', "False") == "True")
ALLOWED_HOSTS = [
    '.thran.cz'
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'modeltranslation',  # must be before django.contrib.admin
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'webpack_loader',
    'import_export',
    'rest_framework',
    'lazysignup',
    'social.apps.django_app.default',  # OAuth
    'tasks',
    'users',
    'practice',
    'flocsweb',
    'flocsweb.tests',
]

APPEND_SLASH = True

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'flocsweb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'flocsweb.wsgi.application'


# Database
DATABASES = {
    "default": dj_database_url.config(default='sqlite:///' +
                                      os.path.join(BASE_DIR, 'db.sqlite3'))
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
USE_I18N = True
USE_L10N = True
USE_TZ = False
# TIME_ZONE = 'UTC'
LANGUAGES = [
    ('cs', 'Czech'),
    ('en', 'English')
]
if ON_PRODUCTION:
    LANGUAGE_DOMAINS = {
        'cs': 'flocs.thran.cz',
        'en': 'en.flocs.thran.cz',
    }
elif ON_STAGING:
    LANGUAGE_DOMAINS = {
        'cs': 'staging.flocs.thran.cz',
        'en': 'en.staging.flocs.thran.cz',
    }
else:
    LANGUAGE_DOMAINS = {
        'cs': 'localhost:8000',
        'en': 'en.localhost:8000',
    }
LANGUAGE_CODE = 'cs'  # fallback language
MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'
#MODELTRANSLATION_TRANSLATION_FILES = (
#    'tasks.models.translation',
#    'blocks.models.translation',
#    'concepts.models.translation',
#)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

# We do this so that django's collectstatic copies or our bundles to the
# STATIC_ROOT or syncs them to whatever storage we use.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'frontend', 'static'),
)
STATIC_ROOT = os.path.join(BASE_DIR, '..', 'static')

# Webpack-Django communication when development
WEBPACK_LOADER = {
    'DEFAULT': {
        'STATS_FILE': os.path.join(BASE_DIR, 'frontend', 'webpack-stats.json')
    }
}

AUTHENTICATION_BACKENDS = (
  'django.contrib.auth.backends.ModelBackend',
  'lazysignup.backends.LazySignupBackend',
  'social.backends.facebook.FacebookOAuth2',
  'social.backends.google.GoogleOAuth2',
)
