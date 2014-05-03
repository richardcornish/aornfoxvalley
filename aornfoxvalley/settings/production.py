"""
Production settings
"""

from aornfoxvalley.settings.base import *


DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = [
    '.aornfoxvalley.org',
    '.aorn.richardcornish.com',
]

MEDIA_ROOT = '/home/richardcornish/webapps/aornfoxvalley_assets/media/'

MEDIA_URL = 'http://aorn-assets.richardcornish.com/media/'

STATIC_ROOT = '/home/richardcornish/webapps/aornfoxvalley_assets/static/'

STATIC_URL = 'http://aorn-assets.richardcornish.com/static/'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'unix:/home/richardcornish/cache/memcached.sock',
    }
}

CACHE_MIDDLEWARE_ALIAS = 'default'
CACHE_MIDDLEWARE_SECONDS = 600
CACHE_MIDDLEWARE_KEY_PREFIX = '3'
