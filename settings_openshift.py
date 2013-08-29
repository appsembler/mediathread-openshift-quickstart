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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mediathread',
        'HOST': get_env_variable('OPENSHIFT_POSTGRESQL_DB_HOST'),
        'PORT': get_env_variable('OPENSHIFT_POSTGRESQL_DB_PORT'),
        'USER': get_env_variable('OPENSHIFT_POSTGRESQL_DB_USERNAME'),
        'PASSWORD': get_env_variable('OPENSHIFT_POSTGRESQL_DB_PASSWORD'),
    }
}

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': get_env_variable('OPENSHIFT_REDIS_DB_HOST') + ':' + get_env_variable('OPENSHIFT_REDIS_DB_PORT'),
        'OPTIONS': {
            'DB': 1,
            'PASSWORD': get_env_variable('OPENSHIFT_REDIS_DB_PASSWORD'),
            'PARSER_CLASS': 'redis.connection.HiredisParser'
        },
    },
    'johnny': {
        'BACKEND': 'johnny.backends.redis.RedisCache',
        'LOCATION': get_env_variable('OPENSHIFT_REDIS_DB_HOST') + ':' + get_env_variable('OPENSHIFT_REDIS_DB_PORT'),
        'OPTIONS': {
            'DB': 1,
            'PASSWORD': get_env_variable('OPENSHIFT_REDIS_DB_PASSWORD'),
            'PARSER_CLASS': 'redis.connection.HiredisParser'
        },
        'JOHNNY_CACHE': True,
    }
}

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

MIDDLEWARE_CLASSES = ('django.middleware.cache.UpdateCacheMiddleware',) + \
                    MIDDLEWARE_CLASSES + \
                    ('django.middleware.cache.FetchFromCacheMiddleware',)

ALLOWED_HOSTS = ['mediathread.appsembler.com', '.rhcloud.com']

COMPRESS_ENABLED = True
COMPRESS_ROOT = STATIC_ROOT
COMPRESS_CSS_HASHING_METHOD = 'content'

SECRET_KEY = get_env_variable('SECRET_KEY')

# Customer.io keys
CUSTOMERIO_SITE_ID = get_env_variable('CUSTOMERIO_SITE_ID')
CUSTOMERIO_API_KEY = get_env_variable('CUSTOMERIO_API_KEY')

# Mailchimp arguments
MAILCHIMP_API_KEY = get_env_variable('MAILCHIMP_API_KEY')
MAILCHIMP_REGISTRATION_LIST_ID = get_env_variable('MAILCHIMP_REGISTRATION_LIST_ID')

# Segment.io key
SEGMENTIO_API_KEY = get_env_variable('SEGMENTIO_API_KEY')
SEGMENTIO_JS_KEY = '3ts2xu858r'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mandrillapp.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = get_env_variable('MANDRILL_USERNAME')
EMAIL_HOST_PASSWORD = get_env_variable('MANDRILL_API_KEY')
DEFAULT_FROM_EMAIL = "support@appsembler.com"
SERVER_EMAIL = "support@appsembler.com"
PUBLIC_CONTACT_EMAIL = "support@appsembler.com"
ACCOUNT_EMAIL_SUBJECT_PREFIX = '[Mediathread] '

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
