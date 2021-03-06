"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+*+&+(y2^9v!%#$a%4va9pr=&-^xxrk9v0xz#q7*w9ks987l!q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [                  # Django自帶應用
    'django.contrib.admin',         # 管理員站點
    'django.contrib.auth',          # 認證授權系統
    'django.contrib.contenttypes',  # 內容類型框架
    'django.contrib.sessions',      # 會話框架
    'django.contrib.messages',      # 消息框架
    'django.contrib.staticfiles',   # 管理靜態文件的框架,有這項才能套用css
    'polls.apps.PollsConfig',
    'shop',                         # 不做怎麼知道系列
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {    # DIRS: 是一個包含多个系统目录的文件列表，用于在载入 Django 模板时使用的待搜索路径。
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 讓templates可運行非內建資料
        # 這項 DIRS 可以決定我們的 templates 路徑
        # 以這邊留空來講，我的 html 就放在 shop/templates/shop/ 底下
        # 在 views.py 就可以用 'shop/shop.html' 來取用
        # 所以留空就代表是預設在 app 資料夾底下的 templates/ (真的嗎＝＝？
        'DIRS': [os.path.join(BASE_DIR, 'templates'),
                 os.path.join(BASE_DIR, 'shop', 'templates', 'shop')],
        # 使DjangoTemplates，在每個INSTALLED_APPS中找templates子目錄
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

WSGI_APPLICATION = 'mysite.wsgi.application'
# WSGI_APPLICATION = 'wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

# 決定我們的 css, javascript, images 放在哪裡
# 我們這邊使用預設的 '/static/'
# css, js, imgs 等的檔案，就放在 app 資料夾底下的 static/
# 而取用方式，舉例 {% static 'css/open-iconic-bootstrap.min.css' %}
STATIC_URL = '/static/'

# 今天的重點之一，上傳產品圖片後，會存放的地方
# Media root for storing uploads in model
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 本來字不會變色，加了這行就可了
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'polls/static')]

