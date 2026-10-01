from django.test import TestCase

# Create your tests here.
from .models import Machine

class MachineModelTests(TestCase):
    def test_machine_creation(self):
        self.assertEqual(Machine.objects.count(),0)
        Machine.objects.create(nom="CNC",prix=28_000, duree_de_vie=10, cout_de_maintenance=12, superficie=10)
        self.assertEqual(Machine.objects.count(),1)