from __future__ import absolute_import, unicode_literals

# Celery'i başlat
from .celery import app as celery_app

__all__ = ['celery_app']
