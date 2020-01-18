"""
Django settings for website project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'urf70#*=7xs=xq(zg6ll#(glzd(v3u46ptrf*^lkm&y#quwchl'

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
    'rest_framework_swagger',
    'django_elasticsearch_dsl_drf',
    'django_elasticsearch_dsl',
    'oauth2_provider',
    'core',
    'users',
    'chatting',
]


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'oauth2_provider.middleware.OAuth2TokenMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'website.urls'

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

WSGI_APPLICATION = 'website.wsgi.application'

OAUTH2_PROVIDER = {
    # this is the list of available scopes
    'SCOPES': {
        'read': 'Read scope', 
        'write': 'Write scope', 
        'groups': 'Access to your groups'
    }
}

SUB_DIR = os.path.basename(os.path.dirname(__file__))
DATABASE_ROUTERS = [
    '{}.database_router.DatabaseAppsRouter'.format(SUB_DIR)
]
DATABASE_APPS_MAPPING = {'potpourri2':'test','EL':'el'}

REST_FRAMEWORK = { 
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
    ), 
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema'
} 

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'NAME': 'potpourri',
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'db', # this need to same of the dockerfile
        'USER': 'root',
        'PASSWORD': '123456',
        'OPTIONS': {
              "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",                                                              
        }
    }
}


ELASTICSEARCH_DSL = {
    'default': {
        'hosts': 'localhost:9200'
    },
}

ELASTICSEARCH_DSL_INDEX_SETTINGS = {
    'number_of_shards': 1
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates').replace('\\', '/')],
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

SWAGGER_SETTINGS = {
    "api_version": 'v0.1',
    "DEFAULT_GENERATOR_CLASS": "rest_framework.schemas.generators.BaseSchemaGenerator",
    'SECURITY_DEFINITIONS': {
        'api_key': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization'
        }
    },
    'LOGIN_URL': 'rest_framework:login',
    'LOGOUT_URL': 'rest_framework:logout',
    'SHOW_REQUEST_HEADERS': True,
    'USE_SESSION_AUTH': True,
    'JSON_EDITOR': True,
    "is_authenticated": False,
    "is_superuser": False,
}

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
