# djangomyblog\blog\urls.py

from django.urls import path
from .views import about, home

urlpatterns = [
    path('', home),
    path('about/', about),
]