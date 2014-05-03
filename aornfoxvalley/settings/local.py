from aornfoxvalley.settings.base import *


DEBUG = True

MEDIA_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../', 'aornfoxvalley_media'))

STATIC_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../', 'aornfoxvalley_media/static'))

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    PROJECT_ROOT + '/static/',
)

TEMPLATE_DIRS = (
    PROJECT_ROOT + '/templates/',
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

