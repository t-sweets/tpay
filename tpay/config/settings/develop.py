from .base import *

DEBUG = True

SECRET_KEY = 'aqzp*s_)$7x%8f3u_+gf2*q2ex4c-@+b0b9(c%_p%y0spj82=m'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '3307',
    }
}
