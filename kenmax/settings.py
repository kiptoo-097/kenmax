"""
Django settings for kenmax project.
"""

import os
from pathlib import Path

# Build paths
BASE_DIR = Path(__file__).resolve().parent.parent

# Security
SECRET_KEY = 'django-insecure-rw_%l(cbqsz&hwx94ea4g+4^na^$7qjl%(9++_0eb9-#@-2j$p'  # Generate a new one for production
DEBUG = False  # Disable in production!
ALLOWED_HOSTS = ['185.113.249.133', 'kenmax.co.ke', 'www.kenmax.co.ke', '127.0.0.1']

# Application definition
INSTALLED_APPS = [
    'django.contrib.staticfiles',  # Only what's needed for maintenance page
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# Template settings (minimal for maintenance page)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',  # Only needed if using admin
            ],
        },
    },
]

# Static files
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Disable unused components
DATABASES = {}  # No database needed for static page
AUTH_PASSWORD_VALIDATORS = []
ROOT_URLCONF = 'kenmax.urls'
WSGI_APPLICATION = 'kenmax.wsgi.application'

