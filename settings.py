# -*- coding: utf-8 -*-
# Django settings for imgnation project.

import sys
import os


def rel(*x):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)


DEBUG = True
TEMPLATE_DEBUG = DEBUG


ADMINS = (
    # ('Your Name', 'your_email@example.com'),
	('Bruno Gama', 'bruno@imgnation.com.br')
)


MANAGERS = ADMINS


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'imgn.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Sao_Paulo'


# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
ugettext = lambda s: s


LANGUAGE_CODE = 'pt_BR'


LANGUAGES = (
    ('pt-br', 	ugettext(u'Português')),
    ('en', 		ugettext(u'English')),
)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True


# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True


# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = rel('media')


# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'


# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = rel('static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/assets/'


# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/assets/admin/'
# ADMIN_MEDIA_PREFIX = '/assets/grappelli/'


# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
	rel('site-theme'),
)


# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
	'django.contrib.staticfiles.finders.FileSystemFinder',
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
	'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


# Make this unique, and don't share it with anybody.
SECRET_KEY = 'e8ec3txx)t_gl1e7-tn-r#w1r#5a-d5sd&%%iz2lxa@ew-s6!l'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.Loader',
	'django.template.loaders.app_directories.Loader',

	# "django.contrib.auth.context_processors.auth",
	# "django.core.context_processors.request",
	# "django.core.context_processors.i18n",
	# 'django.contrib.messages.context_processors.messages',
	# 'django.template.loaders.eggs.Loader',
	'django.template.loaders.app_directories.load_template_source',
)



TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',

    # "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
    # "django.core.context_processors.i18n",
    # 'django.contrib.messages.context_processors.messages',
)


MIDDLEWARE_CLASSES = (
	'annoying.middlewares.StaticServe',
	
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'urli18n.middleware.UrlPathTransformMiddleware',
)


ROOT_URLCONF = 'imgnation.urls'


TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
	rel('templates'),
)


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'django.contrib.sitemaps',
	'urli18n',
	'rosetta',
	'grappelli.dashboard',
	'grappelli',
	'filebrowser',
	'mailer',
	'robots',
	'notification',
    'django.contrib.admin',
	# 'django.contrib.flatpages',

	'imgnation.portfolio',
)


GRAPPELLI_ADMIN_TITLE = "<a href=\"http://www.imgnation.com.br/\" style=\"color:white;\">IMGNATION Studios</a>"


GRAPPELLI_INDEX_DASHBOARD = 'imgnation.dashboard.CustomIndexDashboard'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


# django-urli18n settings 
URLI18N_ALWAYS_SHOW_LANGUAGE = True
URLI18N_INCLUDE_PATHS = ['/', 'about/', 'games/', 'apps/', 'blog/', 'contact/']

EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025