from os.path import abspath, dirname, join

from django.conf import settings

# fetch Django's project directory
DJANGO_ROOT = dirname(dirname(abspath(__file__)))

# fetch the project_root
PROJECT_ROOT = dirname(DJANGO_ROOT)

LOCALE_PATHS = (
    join(PROJECT_ROOT, 'django_xmlrpc/locale'),
)