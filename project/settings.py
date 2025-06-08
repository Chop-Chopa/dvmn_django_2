from environs import Env
import os

env = Env()
env.read_env()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['localhost', '127.0.0.1'])

DATABASES = {
    'default': {
        'ENGINE': env.str('DB_ENGINE', ''),
        'HOST': env.str('DB_HOST', ''),
        'PORT': env.int('DB_PORT', 5432),
        'NAME': env.str('DB_NAME', ''),
        'USER': env.str('DB_USER', ''),
        'PASSWORD': env.str('DB_PASSWORD', ''),
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = env.str('APP_SECRET_KEY', 'your-default-secret-key')

DEBUG = env.bool('DEBUG', default=False)

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]

USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
