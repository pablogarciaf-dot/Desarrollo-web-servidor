from django.urls import path
from . import views

app_name = 'calendario'

urlpatterns = [
    # /calendario/ -> redirige a la fecha de hoy
    path('', views.hoy, name='hoy'),
    # Url genérica: coincide con cualquier texto, por eso va la última
    path('<str:fecha>', views.calendario, name='calendario'),
]
