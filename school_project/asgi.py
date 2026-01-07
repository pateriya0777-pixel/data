"""
ASGI config for school_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from fastapi import FastAPI
from .api import app as fastapi_app

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'school_project.settings')

# 1. Get the standard Django ASGI app
application = get_asgi_application()

# 2. Combine them
# We wrap the Django app inside FastAPI (or vice versa, but this way is cleaner for sub-apps)
# Actually, the easiest way is to use FastAPI as the main entry point 
# and mount Django, OR just serve them together.

# SIMPLIFIED APPROACH:
# We will use Starlette's Mount to attach FastAPI to Django's URL handling 
# is hard. Instead, let's just make a master FastAPI app that holds both.


from starlette.middleware.wsgi import WSGIMiddleware
from django.core.wsgi import get_wsgi_application

# Use WSGI for Django (Standard)
django_wsgi_app = get_wsgi_application()

# Create a main wrapper
master_app = FastAPI()

# Mount FastAPI at /api
master_app.mount("/api", fastapi_app)

# Mount Django at root "/"
# We wrap Django in a middleware so it can speak to the ASGI server
master_app.mount("/", WSGIMiddleware(django_wsgi_app))