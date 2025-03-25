from __future__ import absolute_import, unicode_literals

# Delay Celery import to prevent AppRegistryNotReady error
import django
django.setup()

from .celery import app as celery_app

__all__ = ('celery_app',)