from django.urls import path
from . import views

app_name = 'tres_en_raya'

urlpatterns = [
    path('', views.tres_en_raya, name='tres_en_raya'),
]
