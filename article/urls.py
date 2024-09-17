from django.urls import path
from . import views

app_name="article"

urlpatterns = [
    path('new/',views.new,name="new"),
]
