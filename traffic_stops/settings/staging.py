from traffic_stops.settings.base import *

os.environ.setdefault('CACHE_HOST', '127.0.0.1:11211')
os.environ.setdefault('BROKER_HOST', '127.0.0.1:5672')

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES['default']['NAME'] = 'traffic_stops_staging'
DATABASES['default']['USER'] = 'traffic_stops_staging'
DATABASES['default']['HOST'] = os.environ.get('DB_HOST', '')
DATABASES['default']['PORT'] = os.environ.get('DB_PORT', '')
DATABASES['default']['PASSWORD'] = os.environ['DB_PASSWORD']
DATABASES['traffic_stops_nc']['NAME'] = 'traffic_stops_staging'
DATABASES['traffic_stops_nc']['USER'] = 'traffic_stops_staging'
DATABASES['traffic_stops_nc']['HOST'] = os.environ.get('DB_HOST', '')
DATABASES['traffic_stops_nc']['PORT'] = os.environ.get('DB_PORT', '')
DATABASES['traffic_stops_nc']['PASSWORD'] = os.environ['DB_PASSWORD']

PUBLIC_ROOT = '/var/www/traffic_stops/public/'

STATIC_ROOT = os.path.join(PUBLIC_ROOT, 'static')

MEDIA_ROOT = os.path.join(PUBLIC_ROOT, 'media')

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '%(CACHE_HOST)s' % os.environ,
    }
}

EMAIL_SUBJECT_PREFIX = '[Traffic Stops Staging] '
ADMINS = (
    ('Colin Copeland', 'ccopeland@codeforamerica.org'),
    ('Andy Shapiro', 'shapiromatron@gmail.com'),
    ('Dylan Young', 'dylanjamesyoung@gmail.com'),
)
MANAGERS = ADMINS

DEFAULT_FROM_EMAIL = 'no-reply@codeforamerica.org'

COMPRESS_ENABLED = True

SESSION_COOKIE_SECURE = True

SESSION_COOKIE_HTTPONLY = True

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(';')

# Uncomment if using celery worker configuration
BROKER_URL = 'amqp://traffic_stops_staging:%(BROKER_PASSWORD)s@%(BROKER_HOST)s/traffic_stops_staging' % os.environ

LOGGING['handlers']['file']['filename'] = '/var/www/traffic_stops/log/traffic_stops.log'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': []
}
