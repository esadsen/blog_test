from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# Django'nun default ayarlarını kullanır
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')

app = Celery('blog')

# Django ayarlarını Celery'ye yükle
app.config_from_object('django.conf:settings', namespace='CELERY')

# Tüm task'leri yükle
app.autodiscover_tasks()

# Periyodik görevler için Celery Beat ayarları
app.conf.beat_schedule = {
    'increment-update-count-every-minute': {
        'task': 'article.tasks.increment_update_count',
        'schedule': crontab(minute='*/1'),
    },
}

app.conf.timezone = 'Europe/Istanbul'

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
