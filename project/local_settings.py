DEBUG = True

SECRET_KEY = 'super-secure-hash'

MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/vagrant/myrestproject/src/api/project/media'
STATIC_URL = '/static/'
STATIC_ROOT = '/home/vagrant/myrestproject/src/api/project/collected_static'


# -----------------
# Database
# -----------------

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'norm',
        'USER': 'norm',
        'PASSWORD': 'qwe123',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}


# -----------------
# Cache
# -----------------

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'PARSER_CLASS': 'redis.connection.HiredisParser',
        }
    }
}


# -----------------
# Celery
# -----------------

BROKER_URL = 'redis://127.0.0.1:6379/2'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/3'


# -----------------
# Tornado
# -----------------

TORNADO_APP_PORT = 9000
TORNADO_APP_ADDRESS = '127.0.0.1'


# -----------------
# Project
# -----------------

SITE_URL = 'http://myrest.local'
API_URL = 'http://api.myrest.local'
