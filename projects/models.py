from django.db import models

class ChemicalElement(models.Model):
    atomic_number = models.CharField(max_length=30)  # e.g., "1" for Hydrogen
    symbol = models.CharField(max_length=30)  # e.g., "H" for Hydrogen
    name = models.CharField(max_length=30)  # e.g., "Hydrogen"
    atomic_mass = models.CharField(max_length=30)  # e.g., "1.00794(4)"
    electronic_configuration = models.CharField(max_length=30)  # e.g., "1s1"
    electronegativity = models.CharField(max_length=30, null=True, blank=True)  # e.g., "2.2"
    atomic_radius = models.CharField(max_length=30, null=True, blank=True)  # e.g., "37"
    ion_radius = models.CharField(max_length=30, null=True, blank=True)  # e.g., "unknown"
    van_der_waals_radius = models.CharField(max_length=30, null=True, blank=True)  # e.g., "120"
    ionization_energy = models.CharField(max_length=30, null=True, blank=True)  # e.g., "1312"
    electron_affinity = models.CharField(max_length=30, null=True, blank=True)  # e.g., "-73"
    oxidation_states = models.CharField(max_length=30, null=True, blank=True)  # e.g., "-1, 1"
    standard_state = models.CharField(max_length=30, null=True, blank=True)  # e.g., "gas"
    bonding_type = models.CharField(max_length=30, null=True, blank=True)  # e.g., "diatomic"
    melting_point = models.CharField(max_length=30, null=True, blank=True)  # e.g., "14"
    boiling_point = models.CharField(max_length=30, null=True, blank=True)  # e.g., "20"
    density = models.CharField(max_length=30, null=True, blank=True)  # e.g., "0.0000899"
    group_block = models.CharField(max_length=30, null=True, blank=True)  # e.g., "nonmetal"
    year_discovered = models.CharField(max_length=30, null=True, blank=True)  # e.g., "1766"
    block = models.CharField(max_length=30, null=True, blank=True)  # e.g., "s"
    cpk_hex_color = models.CharField(max_length=30, null=True, blank=True)  # e.g., "FFFFFF"
    period = models.CharField(max_length=30, null=True, blank=True)  # e.g., "1"
    group = models.CharField(max_length=30, null=True, blank=True)  # e.g., "1"
