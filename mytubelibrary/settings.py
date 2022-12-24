"""
Django settings for mytubelibrary project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
from django.contrib.messages import constants
from decouple import config

# ----------------------------------------------------------
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# ----------------------------------------------------------
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# ----------------------------------------------------------
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

# ----------------------------------------------------------
# Allowed Hosts
# --- development --- #
if DEBUG:
    ALLOWED_HOSTS = []

# --- Production --- #
if not DEBUG:
    ALLOWED_HOSTS = [config('ALLOWED_HOSTS')]

# ----------------------------------------------------------
# SSL and Cookies
# ----- Production ----- #
if not DEBUG:
    # SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True


# ----------------------------------------------------------
# Application definition

INSTALLED_APPS = [
    # --- Accounts --- #
    'usuarios',

    # --- Django Apps --- #
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # --- my apps --- #
    'base',
    'canais',
    'playlists',

    # --- Apps secondary --- #
    'django_cleanup.apps.CleanupConfig',
]

# --- Only for use whit Cloudinary media files storage --- #
if not DEBUG:
    INSTALLED_APPS[7:7] = 'cloudinary_storage', 'cloudinary'
    

# ----------------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ----------------------------------------------------------
ROOT_URLCONF = 'mytubelibrary.urls'

# ----------------------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ----------------------------------------------------------
WSGI_APPLICATION = 'mytubelibrary.wsgi.application'


# ----------------------------------------------------------
# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# --- SQLite --- #
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# --- PostgreSQL --- #
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': config('NAME_DB'),
#         'USER': config('USER_DB'),
#         'PASSWORD': config('PASSWORD_DB'),
#         'HOST': config('HOST_DB'),
#         'PORT': config('PORT_DB'),
#     }
# }

# --- PostgreSQL in Heroku--- #
# --- Development --- #
if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': config('NAME_DB'),
            'USER': config('USER_DB'),
            'PASSWORD': config('PASSWORD_DB'),
            'HOST': config('HOST_DB'),
            'PORT': config('PORT_DB'),
        }
    }

# --- Prodution --- #
if not DEBUG:
    import dj_database_url

    DATABASES = {
        'default': dj_database_url.config(
            conn_max_age=600,
            ssl_require=True
        )
    }


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


# ----------------------------------------------------------
# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# ----------------------------------------------------------
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# --- development --- #
if DEBUG:
    STATIC_ROOT = BASE_DIR / 'staticfiles'
    MEDIA_ROOT = BASE_DIR / 'media'

# --- Production --- #
if not DEBUG:
    # STATIC_ROOT = config('STATIC_ROOT')
    # MEDIA_ROOT = config('MEDIA_ROOT')

    # --- For Heroku --- #
    STATIC_ROOT = BASE_DIR / 'staticfiles'
    MEDIA_ROOT = BASE_DIR / 'media'

    # --- Only for use whit Cloudinary media files storage --- #
    CLOUDINARY_STORAGE = {
        'CLOUD_NAME': config('CLOUD_NAME'),
        'API_KEY': config('API_KEY'),
        'API_SECRET': config('API_SECRET')
    }

    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


# ----------------------------------------------------------
# --- Email --- #

# --- development --- #
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# --- Production --- #
if not DEBUG:
    EMAIL_HOST = config('EMAIL_HOST')
    EMAIL_HOST_USER = config('EMAIL_HOST_USER')
    EMAIL_PORT = config('EMAIL_PORT', cast=int)
    # EMAIL_USE_TLS = True
    EMAIL_USE_SSL = True
    EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
    DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')

    ADMINS = [(config('SUPER_USER'), config('EMAIL'))]
    MANAGERS = ADMINS


# ----------------------------------------------------------
# --- Custom User Model --- #
AUTH_USER_MODEL = 'usuarios.CustomUsuario'


# ----------------------------------------------------------
# --- Login Lougout User --- #
LOGIN_REDIRECT_URL = 'index'
LOGOUT_REDIRECT_URL = 'index'


# ----------------------------------------------------------
# Messages
MESSAGE_TAGS = {
    constants.ERROR: 'alert-danger',
    constants.WARNING: 'alert-warning',
    constants.DEBUG: 'alert-info',
    constants.SUCCESS: 'alert-success',
    constants.INFO: 'alert-info',
}
