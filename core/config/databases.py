# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'HOST': 'db',
#         'PORT': '5432',
#         'NAME': 'postgres',
#         'USER': 'postgres',
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db',
        'USER': 'root',
        'PASSWORD': 'example',
        'HOST': 'db',
        'PORT': 3306,
    }
}
# from .consts import DB_DIR
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': DB_DIR,
#     }
# }