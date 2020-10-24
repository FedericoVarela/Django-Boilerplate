from django.conf.global_settings import CSRF_COOKIE_SECURE
from .base import *

DEBUG = False

# TODO: Add allowed hosts
ALLOWED_HOSTS = []


LOGGING = {
    'version': 1,
    'loggers': {
        '{{ project_name }}': {
            'level': "INFO"
        }
    }
}

# For HTTPS
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True