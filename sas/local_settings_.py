# edit and rename to local_settings.py

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Me', 'my@myself.I'),
)
MANAGERS = ADMINS

DATABASES = {
  'default': {
    'ENGINE'  : 'django.db.backends.sqlite3',
    'NAME'    : 'sas.db',
    'USER'    : '',
    'PASSWORD': '',
    'HOST'    : '',
    'PORT'    : '',
  }
}

DEFAULT_FROM_EMAIL = 'webmaster@springaccounts.admin-box.com'
SERVER_EMAIL       = 'webmaster@springaccounts.admin-box.com'
