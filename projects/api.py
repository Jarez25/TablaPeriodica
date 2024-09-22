from .models import ChemicalElement
from rest_framework import viewsets, permissions
from .serializers import ChemicalElementSerializer


class ChemicalElementViewSet(viewsets.ModelViewSet):
    queryset = ChemicalElement.objects.all()
    permission_classes = [permissions.AllowAny] 
    serializer_class = ChemicalElementSerializer
