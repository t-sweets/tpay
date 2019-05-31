from .base import *

SECRET_KEY = os.environ['SECRET_KEY']

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['MYSQL_DATABASE'],
        'USER': os.environ['MYSQL_USER'],
        'PASSWORD': os.environ['MYSQL_PASSWORD'],
        'HOST': os.environ['MYSQL_HOSTNAME'],
        'PORT': '3306',
    }
}

# LDAP Settings
AUTHENTICATION_BACKENDS = (
    "django_python3_ldap.auth.LDAPBackend",
)

LDAP_AUTH_URL = "ldap://192.168.189.4"
LDAP_AUTH_USE_TLS = False
LDAP_AUTH_SEARCH_BASE = "ou=people,dc=t-lab,dc=cs,dc=teu,dc=ac,dc=jp"
LDAP_AUTH_USER_FIELDS = {
    "username": "uid",
    "email": "mail",
}
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "django_python3_ldap": {
            "handlers": ["console"],
            "level": "ERROR",
        },
    },
}