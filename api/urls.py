# api/urls.py
from django.urls import path
from .views import get_news

urlpatterns = [
    path('get/', get_news, name='get_news'),
]
