from rest_framework import serializers
from .models import ChemicalElement

class ChemicalElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChemicalElement
        fields = [
            'atomic_number',
            'symbol',
            'name',
            'atomic_mass',
            'electronic_configuration',
            'electronegativity',
            'atomic_radius',
            'ion_radius',
            'van_der_waals_radius',
            'ionization_energy',
            'electron_affinity',
            'oxidation_states',
            'standard_state',
            'bonding_type',
            'melting_point',
            'boiling_point',
            'density',
            'group_block',
            'year_discovered',
            'block',
            'cpk_hex_color',
            'period',
            'group',
        ]


# from rest_framework import viewsets
# from .models import ChemicalElement
# from .serializers import ChemicalElementSerializer

# class ChemicalElementViewSet(viewsets.ModelViewSet):
#     queryset = ChemicalElement.objects.all()
#     serializer_class = ChemicalElementSerializer
