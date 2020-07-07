import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


STATIC_URL = '/static/'
STATIC_ROOT = STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')
DB_DIR = os.path.join(BASE_DIR, 'bd.sqlite3')