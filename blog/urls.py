from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from article.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('articles/', include('article.urls')),
    path('', index, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

