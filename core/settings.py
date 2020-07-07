import os

from core.config.installed_apps import *
from core.config.middleware import *
from core.config.templates import *
from core.config.auth_password_validators import *
from core.config.youtube_api import *
from core.config.rest_framework import *
from core.config.celery import *
from core.config.databases import *
from core.config.consts import *


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '9-63bn!fqprly%^ok77r=gg8t3v5lc$co&el-ysacovz2r7hk!'

DEBUG = True

ALLOWED_HOSTS = ['*']

ROOT_URLCONF = 'core.urls'

WSGI_APPLICATION = 'core.wsgi.application'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True