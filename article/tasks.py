from celery import shared_task
from .models import Article

#Dakikada bir update_count'u 1 arttıran task oluşturdum.
@shared_task
def increment_update_count():
    articles = Article.objects.all()
    for article in articles:
        article.update_count += 1
        article.save()
