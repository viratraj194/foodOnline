from pathlib import Path
import os
from django.db.models import BigAutoField



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*8_6y5k5a6w3(-1r*6sa-jh_c!llj&oz+(d!i&b_-&na%fe34p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 'True'

ALLOWED_HOSTS = ['172.105.58.30','127.0.0.1','desibhojan.shop','www.desibhojan.shop']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'vendor',
    'menu',
    'marketplace',
    'django.contrib.gis',
    'customers',
    'orders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'orders.request_object.RequestObjectMiddleware',#custom middleware is created to access the request objects in models.py
]

ROOT_URLCONF = 'foodonline.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'accounts.context_processors.get_vendor',
                'accounts.context_processors.get_user_profile',
                'accounts.context_processors.get_google_api',
                'accounts.context_processors.get_paypal_clint_id',
                'marketplace.context_processors.get_cart_counter',
                'marketplace.context_processors.get_cart_amounts',
                
            ],
        },
    },
]

WSGI_APPLICATION = 'foodonline.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'foodonline',
        'USER': 'postgres',
        'PASSWORD': '7070158485',
        'HOST': 'localhost',
    }
}

AUTH_USER_MODEL = 'accounts.User'


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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR /'static'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'foodonline/static'),
]

#media file
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

#email configuration
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER ='rajofficial513@gmail.com'
EMAIL_HOST_PASSWORD = 'qxqmxsywxvpqxgmx'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'foodonline Marketplace <rajofficial513@gmail.com>'


GOOGLE_API_KEY = 'AIzaSyDDnv36aSn8Ksv2FNb_YR-HPlsue0VGr-s'

DEFAULT_AUTO_FIELD='django.db.models.AutoField'


if DEBUG == True:
    os.environ['PATH'] = os.path.join(BASE_DIR, 'venv\Lib\site-packages\osgeo') + ';' + os.environ['PATH']
    os.environ['PROJ_LIB'] = os.path.join(BASE_DIR, 'venv\Lib\site-packages\osgeo\data\proj') + ';' + os.environ['PATH']
    GDAL_LIBRARY_PATH = os.path.join(BASE_DIR, 'venv\Lib\site-packages\osgeo\gdal304.dll')




PAYPAL_CLINT_ID = 'AXfyS-RTg6uhsghPMQxLampg6iLFtKov_9Vn_uhHgX379oaaLsEueBh7fMNV2lspOjUVqcRAsSXeTwHd'

RZP_KEY_ID = 'rzp_test_nVilJHkobwgrOf'
RZP_KEY_SECRET = 'zc8SEqaAd9UyNXFQm5cf5GYJ'


SECURE_CROSS_ORIGIN_OPENER_POLICY = 'same-origin-allow-popups'