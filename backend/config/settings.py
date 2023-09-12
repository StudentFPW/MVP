"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-3x_4_vx_1se8@dwc%*y2lju$zu(&8y$#7p%wj)nj2_i!bg*b5p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'djoser',
    'sslserver',
    'drf_yasg',
    'drf_social_oauth2',
    'social_django',
    'oauth2_provider',
    'rest_framework.authtoken',
    'django_celery_beat',

    'djangoscrapy',
    'main',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect'
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators
AUTH_USER_MODEL = 'main.User'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'Europe/Moscow'  # DO NOT CHANGE IT.

USE_I18N = True

USE_TZ = False  # DO NOT CHANGE IT.

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# DRF
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        'drf_social_oauth2.authentication.SocialAuthentication',
    ),

    # 'DEFAULT_PERMISSION_CLASSES': [ # TODO UNCOMMENT THIS FOR YOUR REQUIREMENTS
    #     'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    # ]
}

DJOSER = {
    'LOGIN_FIELD': 'email',
    'PASSWORD_RESET_CONFIRM_URL': 'auth/password/reset/confirm/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL': 'auth/username/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': 'auth/activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
    'SERIALIZERS': {
        'current_user': 'main.serializers.CustomUserSerializer'
    },
    'USER_CREATE_PASSWORD_RETYPE': True,
    'SET_PASSWORD_RETYPE': True,
}

EMAIL_CHANGE_CONFIRM_URL = 'auth/change/email/{uid}/{token}'

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"  # TODO для разработки
# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
DEFAULT_FROM_EMAIL = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_USE_SSL = True

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.getenv('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.getenv('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile',
]

SOCIAL_AUTH_VK_OAUTH2_KEY = os.getenv('SOCIAL_AUTH_VK_OAUTH2_KEY')
SOCIAL_AUTH_VK_OAUTH2_SECRET = os.getenv('SOCIAL_AUTH_VK_OAUTH2_SECRET')
SOCIAL_AUTH_VK_APP_USER_MODE = 2

SOCIAL_AUTH_YANDEX_OAUTH2_KEY = os.getenv('SOCIAL_AUTH_VK_OAUTH2_KEY')
SOCIAL_AUTH_YANDEX_OAUTH2_SECRET = os.getenv('SOCIAL_AUTH_VK_OAUTH2_SECRET')

AUTHENTICATION_BACKENDS = (
    'social_core.backends.yandex.YandexOAuth2',
    'social_core.backends.vk.VKOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    'drf_social_oauth2.backends.DjangoOAuth2',
    'main.backends.AuthBackend',
)

# Если вы используете Redis Labs, то переменные CELERY_BROKER_URL и CELERY_RESULT_BACKEND должны строиться по шаблону:
#       redis://логин:пароль@endpoint:port

CELERY_BROKER_URL = f'redis://default:P2esA8YJJqVFjdW1kgGxl1jGSqmFgxEd' \
                    f'@redis-16433.c8.us-east-1-3.ec2.cloud.redislabs.com:16433'

CELERY_RESULT_BACKEND = f'redis://default:P2esA8YJJqVFjdW1kgGxl1jGSqmFgxEd' \
                        f'@redis-16433.c8.us-east-1-3.ec2.cloud.redislabs.com:16433'

CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = "Europe/Moscow"  # DO NOT CHANGE IT.
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
