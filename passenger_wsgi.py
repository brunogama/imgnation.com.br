import sys, os

INTERP = os.path.join(os.environ['HOME'], '.virtualenvs', 'imgnation', 'bin', 'python')
if sys.executable != INTERP:
	os.execl(INTERP, INTERP, *sys.argv)

sys.path.append(os.getcwd())
os.environ['DJANGO_SETTINGS_MODULE'] = "imgnation.server_settings"

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
