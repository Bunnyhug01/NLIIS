from django.urls import path
from . import views

urlpatterns = [
    path('', views.process, name = 'process'),
    path('generation', views.generation, name = 'generation'),
    path('help', views.help, name = 'help'),
    path('savedWords', views.savedWords, name = 'savedWords'),
]