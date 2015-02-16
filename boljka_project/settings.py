"""
Django settings for boljka_project project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b29&_364ku+#xedc%!ojq^)ydq!x!v_(^sduz^rp1o%bogpg-r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = (
    'modeltranslation',             # Must be before 'django.contrib.admin'
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'haystack',
    'illness',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

# TEMPLATE_CONTEXT_PROCESSORS = (
#     'django.contrib.messages.context_processors.messages',
#     'django.contrib.auth.context_processors.auth',
# )

ROOT_URLCONF = 'boljka_project.urls'

WSGI_APPLICATION = 'boljka_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'illness',
    }
}

HAYSTACK_CONNECTIONS = {
    'default_en': {
        'ENGINE': 'boljka_project.backend.MultilingualSolrEngine',
        'URL': 'http://127.0.0.1:8983/solr/solr_en',
        'EXCLUDED_INDEXES': ['illness.search_indexes.IllnessSRIndex'],
    },
    'default_sr': {
        'ENGINE': 'boljka_project.backend.MultilingualSolrEngine',
        'URL': 'http://127.0.0.1:8983/solr/solr_sr',
        'EXCLUDED_INDEXES': ['illness.search_indexes.IllnessENIndex'],
    },
}
# Requires default connection
HAYSTACK_CONNECTIONS['default'] = HAYSTACK_CONNECTIONS['default_en']

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

# LANGUAGE_CODE = 'en'
LANGUAGES = (
    ('sr', 'Srpski'),
    ('en', 'English'),
)

TIME_ZONE = 'CET'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATICFILES_DIRS = (
#     BASE_DIR + "/static",
# )

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
)