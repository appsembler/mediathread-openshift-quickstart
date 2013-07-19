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

PROJECT_ROOT = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'mediathread', 'mediathread')

STATIC_ROOT = os.path.join(get_env_variable('OPENSHIFT_REPO_DIR'), 'wsgi', 'static')
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(STATIC_ROOT, 'media')
STATIC_URL = '/static/media/'

COMPRESS_ENABLED = False
COMPRESS_ROOT = STATIC_ROOT
COMPRESS_URL = STATIC_URL

SECRET_KEY = "$#bc!$782^y76@vs3lr+w^qx)&qsuic*ycz%ta_f^cu(1+4($x"
