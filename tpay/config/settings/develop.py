from .base import *

DEBUG = True

SECRET_KEY = 'aqzp*s_)$7x%8f3u_+gf2*q2ex4c-@+b0b9(c%_p%y0spj82=m'

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
