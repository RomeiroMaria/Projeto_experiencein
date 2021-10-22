#arquivo novo caminho: experiencein/perfis/urls.py

#movendo as declarações da rota feita em experiencein/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]