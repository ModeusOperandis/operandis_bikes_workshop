from django.test import TestCase

from .models import *

# Create your tests here.
from .models import Machine


class MachineModelTests(TestCase):
    def test_machine_creation(self):
        self.assertEqual(Machine.objects.count(), 0)
        Machine.objects.create(
            nom="CNC",
            prix=28_000,
            duree_de_vie=10,
            cout_de_maintenance=12,
            superficie=10,
        )
        self.assertEqual(Machine.objects.count(), 1)


# class CoutPointVente(TestCase):
#    def test_cout_pt_vente(self):
#        P = Pays.objects.create(
#           nom="France", tva=0.2, tarif_electrique=0.2, salaire_minimum=12
#      )
#     V = Ville.objects.create(
#        nom="Labège", taxe_immobiliere=0.2, prix_metre_carre=2000, pays=P
#   )
#  M1 = Machine.objects.create(
#     nom="Machine1",
#    prix=10000,
#   duree_de_vie="10",
#  cout_de_maintenance=0,
# superficie=1,
# )
# M2 = Machine.objects.create(
#    nom="Machine2",
#    prix=5000,
#    duree_de_vie="10",
#    cout_de_maintenance=0,
#    superficie=1,
# )
# Produit1 = Produit.objects.create(
#    nom="Tubes d'Acier",
#    prix_de_vente=10,
#    duree_de_vie=500,
#    nombre_par_palette=50,
# )
# Produit2 = Produit.objects.create(
#    nom="Câbles", prix_de_vente=10, duree_de_vie=500, nombre_par_palette=300
# )
# qp1 = QuantiteProduit.objects.create()
# S = Stock.objects.create(quantite_produit=0, palettes_max=1000)

# Point_de_vente.objects.create(
#    nom="Operandis_Store",
# )
# self.assertEqual()
