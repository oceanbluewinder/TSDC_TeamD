"""
Django settings for TSDC project.

Based on 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import posixpath

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7203c285-ebd1-4387-bde2-6f90843645d6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application references
# https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-INSTALLED_APPS
INSTALLED_APPS = [
    # Add your apps here to enable them
    'app',#�_�lapp
    'food',#���~�~
    'financial',#���ķ~
    'shipping',#��B�~�B2022/03/01�[�J
    'chA',#chA�M�D�ʾ��B2022/03/09�[�J
    'chB',#chB�M�D�ؼСB2022/03/09�[�J
    'chC',#chC�M�D��{�B2022/03/09�[�J
    'chD',#chD��z�Ѳ������D�J���x���B2022/03/09�[�J
    'chE',#chE���ά����D�J���x���B2022/03/09�[�J
    'chF',#chF���g�����D�J���x���B2022/03/09�[�J
    'chG',#chG�p�զX�@�D�J���x���B2022/03/09�[�J
    'chH',#chH�M�D�i��2022/03/09�[�J
    'chI',#chI�峹�d�Ҥ@2022/03/09�[�J
    'chJ',#chJ�峹�d�ҤG2022/03/09�[�J
    'django.contrib.admin',# admin��O�޲z���I
    'django.contrib.auth',# �����{�Ҩt��
    'django.contrib.contenttypes',# ���e���O�ج[
    'django.contrib.sessions',# �^�ܮج[
    'django.contrib.messages',# �T���ج[
    'django.contrib.staticfiles',# �R�A�ɮ׺޲z�ج[
]

# Middleware framework
# https://docs.djangoproject.com/en/2.1/topics/http/middleware/
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'TSDC.urls'

# Template configuration
# https://docs.djangoproject.com/en/2.1/topics/templates/
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

WSGI_APPLICATION = 'TSDC.wsgi.application'
# Database�����ƮwSQL
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/2.1/topics/i18n/
LANGUAGE_CODE = 'zh-hant'
TIME_ZONE = 'asia/Taipei'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

#���R�A�ɮ׳]�w����(��bstaticfiles)
STATIC_URL = '/static/' #�����ؿ��W��
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "staticfiles"),
]
STATIC_ROOT = posixpath.join(*(BASE_DIR.split(os.path.sep) + ['static']))