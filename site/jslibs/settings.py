# Django settings for jslibs project.

import os as _os
from local_settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)
MANAGERS = ADMINS

TIME_ZONE = 'Europe/Berlin'
LANGUAGE_CODE = 'en-us'
USE_I18N = False
USE_L10N = False

SITE_ID = 1

MEDIA_ROOT = _os.path.dirname(__file__) + '/../media/'
MEDIA_URL = ''
STATIC_ROOT = _os.path.dirname(__file__) + '/../static/'
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Don't forget to use absolute paths, not relative paths.
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'reversion.middleware.RevisionMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    _os.path.dirname(__file__) + '/templates/'
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'reversion',
    'libraries',
)

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

# List of non-project top level paths
NON_LIBRARY_PATHS = [
    "about",
    "account",
    "accounts",
    "activity",
    "all",
    "announcements",
    "anywhere",
    "api",
    "api_rules",
    "apirules",
    "api_terms",
    "apps",
    "assets",
    "auth",
    "badges",
    "blog",
    "business",
    "buttons",
    "contacts",
    "devices",
    "download",
    "downloads",
    "faq",
    "favorites",
    "find_sources",
    "find_users",
    "goodies",
    "help",
    "home",
    "inbox",
    "invitations",
    "invite",
    "jobs",
    "libraries",
    "library",
    "list",
    "login",
    "logout",
    "me",
    "media",
    "messages",
    "notifications",
    "nudge",
    "oauth",
    "positions",
    "privacy",
    "project",
    "projects",
    "related",
    "related_projects",
    "replies",
    "rules",
    "search",
    "sent",
    "settings",
    "share",
    "signin",
    "signup",
    "similar_to",
    "static",
    "statistics",
    "terms",
    "tests",
    "tos",
    "translate",
    "trends",
    "update_discoverability",
    "user",
    "users",
    "welcome",
    "widgets",
]
