from django.conf.global_settings import CSRF_COOKIE_SECURE
from .base import *

DEBUG = False

# TODO: Add allowed hosts
ALLOWED_HOSTS = []

# For HTTPS
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True