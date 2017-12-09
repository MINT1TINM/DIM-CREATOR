
"""
WSGI config for DIMCREATOR project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DIMCREATOR.settings")

#abspath = os.path.dirname(__file__)
#sys.path.append(abspath)
#os.chdir(abspath)

application = get_wsgi_application()
