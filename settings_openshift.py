import os
from django.core.exceptions import ImproperlyConfigured
from settings import *


def get_env_variable(var_name):
    """ Get the environment variable or return exception """
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s environment variable" % var_name
        raise ImproperlyConfigured(error_msg)


DEBUG = False
TEMPLATE_DEBUG = DEBUG

PROJECT_ROOT = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'mediathread')
APP_ROOT = os.path.join(PROJECT_ROOT, 'mediathread')

STATIC_ROOT = os.path.join(get_env_variable('OPENSHIFT_REPO_DIR'), 'wsgi', 'static', 'collected_static')
STATIC_URL = '/site_media/'
MEDIA_ROOT = os.path.join(get_env_variable('OPENSHIFT_REPO_DIR'), 'wsgi', 'static', 'media')
MEDIA_URL = '/media/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'media'),
)

ALLOWED_HOSTS = ['.rhcloud.com']

COMPRESS_ENABLED = False
COMPRESS_ROOT = STATIC_ROOT

SECRET_KEY = "$#bc!$782^y76@vs3lr+w^qx)&qsuic*ycz%ta_f^cu(1+4($x"

# Sentry/Raven config
RAVEN_CONFIG = {
    'dsn': get_env_variable('SENTRY_DSN'),
    'timeout': 3,
}

INSTALLED_APPS += (
    'django.contrib.staticfiles',
    'raven.contrib.django.raven_compat',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    }
}
