"""
Django settings for my_doctor project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'rd*14e!dam(_=6n!^=)2*ee73%lkbnnhop2u5w-7!9kuh(unv6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1','doctor-plus.in','www.doctor-plus.in']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'rest_framework',
    'patients',
    'doctors',
    'knox',
    'specialist_type',
    'consultations',
    'appointment',
    'consultant_chat',
    'subscription_plans',
    'frontend',
    'doctorsUI',
    'patientsUI',
    'transactions',
    'executive_details',
    'doctor_payments',
    'patient_wallet_details',
    'feedback_replies',
    'patient_feedbacks',
    'patient_subscription',
    'patient_medical_records',
    'website',
    'online_enquiry',
    'reminders',
    'bill_payments',
    'vedio_chat'
]

MIDDLEWARE = [
    # 'social_django.middleware.SocialAuthExceptionMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'my_doctor.urls'

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

                # 'social_django.context_processors.backends',
                # 'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'my_doctor.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': 'doctor_plus',
#        'USER': 'bstejas_dp',
#        'PASSWORD': 'bstejas_dp1',
#        'HOST': '148.66.136.124',
#        'PORT': '3306',
#        'OPTIONS': {
#            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
#        }
#    }
#}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

REST_FRAMEWORK = {
   'DEFAULT_AUTHENTICATION_CLASSES': (
       'knox.auth.TokenAuthentication',
   ),
}

# AUTHENTICATION_BACKENDS = (

#     'social.backends.google.GoogleOAuth2',
#     'django.contrib.auth.backends.ModelBackend',
# )

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/
DATETIME_FORMAT = '%d-%m-%Y %H:%M:%S' 

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_ROOT= os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'my_doctor/static')
]
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'



# SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '145610180262-e30cgv3sdtul1eu6kplk1q3i3r79h574.apps.googleusercontent.com'
# SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'jzx9qTt54W8JvTNoNt3jSCqK'

# LOGIN_URL = 'http://localhost:8000/login'
# LOGIN_REDIRECT_URL = 'http://localhost:8000/patients/dashboard'

