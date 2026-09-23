from django.db import models

# Create your models here.
class Pays(models.Model):
    nom = models.CharField()
    tva = models.FloatField()
    tarif_electrique = models.FloatField()
    salaire_minimum = models.FloatField()

class Ville(models.Model):
    nom = models.CharField()
    taxe_immobiliere = models.CharField()
    prix_metre_carre = models.FloatField()
    pays = models.ForeignKey(Pays, on_delete=models.PROTECT)

class Lieu(models.Model):
    nom = models.CharField()
    ville = models.ManyToManyField(Ville, on_delete=models.PROTECT)
    superficie = models.FloatField()
    quantite_machines = models.ForeignKey("Quantite_machine", on_delete=models.PROTECT)
    consomation_electrique = models.FloatField()

class Quantite_machine(models.Model):
    type_machine = models.ForeignKey("Machine", on_delete=models.PROTECT)
    nombre = models.IntegerField()

class Machine(models.Model):
    nom = models.CharField()
    prix = models.FloatField()
    duree_de_vie = models.FloatField()
    cout_de_maintenance = models.FloatField()
    superficie = models.FloatField()

class Transport(models.Model):
    nombre_palettes = models.IntegerField()
    cout = models.FloatField()
    delai = models.FloatField()
    depart = models.ForeignKey(Lieu, on_delete=models.PROTECT)
    arrive = models.ForeignKey(Lieu, on_delete=models.PROTECT)

class Operation(models.Model):
    nom = models.CharField()
    operation_suivante = models.ForeignKey("self", on_delete=models.PROTECT) #liste chaînée
    cout = models.FloatField()
    machine = models.ForeignKey(Machine, on_delete=models.PROTECT)
    quantite_produit = models.ManyToManyField(Quantite_produit, on_delete=models.PROTECT)
    heure_de_travail = models.FloatField()
    consomation_electrique = models.FloatField()

class Produit(models.Model):
    nom = models.CharField()
    prix_de_vente = models.FloatField()
    duree_de_vie = models.FloatField()
    nombre_par_palette = models.IntegerField()
    operations = models.ForeignKey(Operation, on_delete=models.PROTECT) #c'est une liste chaînée

class Prix_Produit(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.PROTECT)
    prix_achat = models.FloatField()

class Fournisseur(models.Model):
    produit = models.ManyToManyField(Produit, on_delete=models.PROTECT)
    prix_achat = models.FloatField()

class QuantiteProduit(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.PROTECT)
    nombre = models.IntegerField()

class Stock(models.Model):
    quantite_produit = models.ManyToManyField("Quantite_Produit", on_delete=models.PROTECT)
    palettes_max = models.IntegerField()

class Point_de_vente(models.Model):
    nom = models.CharField()
    lieu = models.ForeignKey(Lieu, on_delete=models.PROTECT)
    heure_de_travail = models.FloatField()
    stock = models.ForeignKey(Stock, on_delete=models.PROTECT)

class Facture(models.Model):
    quantite_produit = models.ManyToManyField("QuantiteProduit", on_delete=models.PROTECT)
    reduction = models.FloatField()
    Point_de_vente = models.ForeignKey(Point_de_vente, on_delete=models.PROTECT)
    client = models.CharField()






