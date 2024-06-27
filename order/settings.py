"""
Django settings for order project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path
# import environ
# env = environ.Env(DEBUG=(bool, False))
# environ.Env.read_env(BASE_DIR / ".env")

from dotenv import load_dotenv
load_dotenv()
import dj_database_url


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-wr764&r@7@64@jzg58x)(_-42vz76zo9@x=ac3&e*thbyvf^rq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# ALLOWED_HOSTS= os.environ.get("ALLOWED_HOSTS").split(" ")
# Security configuration settings

#  make cookies HttpOnly, which means they are not accessible via JavaScript,
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',



    # installed app
    "orders",
    'oidc_provider',
    'rest_framework',
    # 'rest_framework.authtoken',
    "oauth2_provider",
    "drf_yasg",
]
# LOGIN_URL = '/accounts/login/'
LOGIN_URL = '/admin/login/'
USERNAME_FIELD = ['username']

# AUTHENTICATION_BACKENDS = (
#     'django.contrib.auth.backends.ModelBackend',
#     'oidc_provider.backends.OIDCAuthenticationBackend',
# )

# OIDC_USERINFO = 'order.oidc_provider_settings.userinfo'
# OIDC_EXTRA_SCOPE_CLAIMS = 'order.oidc_provider_settings.CustomScopeClaims'

AUTH_USER_MODEL = 'orders.Customer'

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'order.urls'

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


WSGI_APPLICATION = 'order.wsgi.application'
# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
#     ),
#     'DEFAULT_PERMISSION_CLASSES': (
#         'rest_framework.permissions.IsAuthenticated',
#     )
# }

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}


# OAUTH2_PROVIDER = {
#     # this is the list of available scopes
#     'SCOPES': {
#         'read': 'Read scope',
#         'write': 'Write scope',
#         'groups': 'Access to your groups',
#         'introspection': 'Introspect token scope',
#     },
#     'RESOURCE_SERVER_INTROSPECTION_URL': 'http://127.0.0.1:8000/o/introspect/',
#     'RESOURCE_SERVER_AUTH_TOKEN': 'auth_server_admin_token',
# }

# OAUTH2_PROVIDER = {
#     'ACCESS_TOKEN_EXPIRE_SECONDS': 36000,
#     'AUTHORIZATION_CODE_EXPIRE_SECONDS': 600,
#     'REFRESH_TOKEN_EXPIRE_SECONDS': 86400,
#     'OIDC_ENABLED': True,
#     'OIDC_RSA_PRIVATE_KEY': '''-----BEGIN RSA PRIVATE KEY-----
#     ...
#     -----END RSA PRIVATE KEY-----''',
#     'SCOPES': {
#         'openid': 'OpenID Connect scope',
#         'profile': 'Profile scope',
#         'email': 'Email scope',
#     },
# }

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
#

database_url = os.environ.get("DATABASE_URL")
DATABASES = {
    'default': dj_database_url.config(
        default=database_url,
        conn_max_age=600,
        conn_health_checks=True,
    )
}
#
# DATABASES = {
#     "default": {
#         "ENGINE": "django.contrib.gis.db.backends.postgis",
#         "NAME": os.environ["POSTGRES_DB"],
#         "USER": os.environ["POSTGRES_USER"],
#         "PASSWORD": os.environ["POSTGRES_PASSWORD"],
#         "HOST": os.environ["PG_HOST"],
#         "PORT": os.environ["PG_PORT"],
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# STATIC_URL = 'static/'

# STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
