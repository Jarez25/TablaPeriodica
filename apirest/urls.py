from django.contrib import admin
from django.urls import path, include  # Importar 'include' para añadir rutas de la app

urlpatterns = [
    path('admin/', admin.site.urls),
    # Incluir las URLs registradas en la aplicación 'projects'
    path('', include('projects.urls')),  # Ajusta 'projects' al nombre correcto de tu app
]
