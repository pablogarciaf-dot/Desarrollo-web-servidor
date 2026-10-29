from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('contacto/', views.contacto, name='contacto'),
    # Cada app tiene su propio urls.py con su namespace (app_name)
    path('escaparate/', include('escaparate.urls')),
    path('calendario/', include('calendario.urls')),
]
