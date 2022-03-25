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
    'app',#起始app
    'food',#食品業
    'financial',#金融業
    'shipping',#航運業、2022/03/01加入
    'chA',#chA專題動機、2022/03/09加入
    'chB',#chB專題目標、2022/03/09加入
    'chC',#chC專題行程、2022/03/09加入
    'chD',#chD整理股票相關遭遇的困難、2022/03/09加入
    'chE',#chE爬蟲相關遭遇的困難、2022/03/09加入
    'chF',#chF撰寫網站遭遇的困難、2022/03/09加入
    'chG',#chG小組合作遭遇的困難、2022/03/09加入
    'chH',#chH專題展望2022/03/09加入
    'chI',#chI文章範例一2022/03/09加入
    'chJ',#chJ文章範例二2022/03/09加入
    'django.contrib.admin',# admin後臺管理站點
    'django.contrib.auth',# 身份認證系統
    'django.contrib.contenttypes',# 內容型別框架
    'django.contrib.sessions',# 回話框架
    'django.contrib.messages',# 訊息框架
    'django.contrib.staticfiles',# 靜態檔案管理框架
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
# Database內鍵資料庫SQL
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

#跟靜態檔案設定有關(放在staticfiles)
STATIC_URL = '/static/' #虛擬目錄名稱
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "staticfiles"),
]
STATIC_ROOT = posixpath.join(*(BASE_DIR.split(os.path.sep) + ['static']))