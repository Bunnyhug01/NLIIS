from django.urls import path
from . import views

urlpatterns = [
    path('', views.process, name = 'process'),
    path('generation', views.generation, name = 'generation'),
    path('help', views.help, name = 'help'),
    path('savedWords', views.savedWords, name = 'savedWords'),
    path('syntaxAnalysis', views.syntaxAnalysis, name = 'syntaxAnalysis'),
    path('semanticAnalysis', views.semanticAnalysis, name = 'semanticAnalysis'),
    path('chat', views.chat, name = 'chat'),
]