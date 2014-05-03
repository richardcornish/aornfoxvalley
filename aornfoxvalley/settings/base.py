"""
Django settings for aornfoxvalley project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

PROJECT_ROOT = BASE_DIR
REPOSITORY_ROOT = os.path.join(PROJECT_ROOT, os.pardir)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['AORN_SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True


# Application definition

INSTALLED_APPS = (

    # Django apps, by default
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Django apps, for this project
    'django.contrib.admindocs',
    'django.contrib.flatpages',
    'django.contrib.redirects',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'django.contrib.syndication',

    # Personal apps
    'aornfoxvalley.adminplus',
    'aornfoxvalley.flatpages',
    'aornfoxvalley.news',
    'aornfoxvalley.events',
    'aornfoxvalley.speakers',
    'aornfoxvalley.records',
    'aornfoxvalley.members',
    'aornfoxvalley.links',
    'aornfoxvalley.feeds',
    'aornfoxvalley.templatetags',

    # Third-party apps
    'markdown',
    'robots',
    'south',
    'typogrify',

)

MIDDLEWARE_CLASSES = (

    # First for caching
    'django.middleware.cache.UpdateCacheMiddleware',

    # Default middleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Remove "www"
    'aornfoxvalley.middleware.no_www.UrlMiddleware',

    # Redirects middleware
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',

    # Flatpage fallback
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',

    # Last for caching
    'django.middleware.cache.FetchFromCacheMiddleware',

)

ROOT_URLCONF = 'aornfoxvalley.urls'

WSGI_APPLICATION = 'aornfoxvalley.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['AORN_DB_NAME'],
        'USER': os.environ['AORN_DB_USER'],
        'PASSWORD': os.environ['AORN_DB_PASS'],
        'HOST': '',
        'PORT': '',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


# Templates
# https://docs.djangoproject.com/en/1.6/topics/templates/

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    # 'django.template.loaders.eggs.load_template_source',
)

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS

TEMPLATE_CONTEXT_PROCESSORS += (
    'aornfoxvalley.context_processors.site',
    'aornfoxvalley.context_processors.email',
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)


# Project-specific settings

SITE_ID = 1

REMOVE_WWW = True

CONTACT_EMAIL = os.environ['AORN_CONTACT_EMAIL']
