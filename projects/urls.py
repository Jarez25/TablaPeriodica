from rest_framework import routers
from .api import ChemicalElementViewSet

# Crear un enrutador para la API REST
router = routers.DefaultRouter()
# Registrar el conjunto de vistas con la URL correspondiente
router.register('api/chemical', ChemicalElementViewSet, 'chemical')

# Asegúrate de que esto esté correctamente escrito en minúsculas.
urlpatterns = router.urls
