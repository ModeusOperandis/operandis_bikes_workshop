from django.db import models

# Create your models here.
class Pays(models.Model):
    nom = models.CharField()
    tva = models.FloatField()
    tarif_electrique = models.FloatField()
    salaire_minimum = models.FloatField()
    def __str__(self):
            return self.nom
    

class Ville(models.Model):
    nom = models.CharField()
    taxe_immobiliere = models.CharField()
    prix_metre_carre = models.FloatField()
    pays = models.ForeignKey(Pays, on_delete=models.PROTECT)
    def __str__(self):
        return self.nom


class Produit(models.Model):
    nom = models.CharField()
    prix_de_vente = models.FloatField(blank=True, null=True)
    duree_de_vie = models.FloatField()
    nombre_par_palette = models.IntegerField()
    operation = models.ForeignKey("Operation", blank=True, null=True, on_delete=models.PROTECT) #c'est une liste chaînée
    def __str__(self):
            return self.nom
    
class QuantiteProduit(models.Model):
    produit = models.ForeignKey(Produit,  on_delete=models.PROTECT)
    nombre = models.IntegerField()

class Lieu(models.Model):
    nom = models.CharField()
    ville = models.ManyToManyField("Ville")
    superficie = models.FloatField()
    quantite_machines = models.ForeignKey("Quantite_machine", on_delete=models.PROTECT)
    consomation_electrique = models.FloatField()
    def __str__(self):
            return self.nom

class Machine(models.Model):
    nom = models.CharField()
    prix = models.FloatField()
    duree_de_vie = models.FloatField()
    cout_de_maintenance = models.FloatField()
    superficie = models.FloatField()
    def __str__(self):
            return self.nom
    
class Quantite_machine(models.Model):
    type_machine = models.ForeignKey(Machine, blank=True, null=True, on_delete=models.PROTECT)
    nombre = models.IntegerField()



class Transport(models.Model):
    nombre_palettes = models.IntegerField()
    cout = models.FloatField()
    delai = models.FloatField()
    depart = models.ForeignKey(Lieu, on_delete=models.PROTECT, related_name="depart+")
    arrive = models.ForeignKey(Lieu, on_delete=models.PROTECT)

class Operation(models.Model):
    nom = models.CharField(max_length=100)
    operation_suivante = models.ForeignKey("self",blank=True, null=True, on_delete=models.PROTECT) #liste chaînée
    cout = models.FloatField()
    machine = models.ForeignKey(Machine, on_delete=models.PROTECT)
    quantite_produit = models.ManyToManyField("QuantiteProduit", blank=True, null=True)
    heure_de_travail = models.FloatField()
    consomation_electrique = models.FloatField()
    def __str__(self):
            return self.nom



class Prix_Produit(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.PROTECT)
    prix_achat = models.FloatField()

class Fournisseur(models.Model):
    nom = models.CharField()
    produit = models.ManyToManyField(Produit)
    prix_achat = models.FloatField()



class Stock(models.Model):
    quantite_produit = models.ManyToManyField("QuantiteProduit")
    palettes_max = models.IntegerField()

class Point_de_vente(models.Model):
    nom = models.CharField()
    lieu = models.ForeignKey(Lieu, on_delete=models.PROTECT)
    heure_de_travail = models.FloatField()
    stock = models.ForeignKey(Stock, on_delete=models.PROTECT)
    def __str__(self):
                return self.nom

class Facture(models.Model):
    numero_facture = models.CharField(max_length=100)
    quantite_produit = models.ManyToManyField("QuantiteProduit")
    reduction = models.FloatField()
    Point_de_vente = models.ForeignKey(Point_de_vente, on_delete=models.PROTECT)
    client = models.CharField()
    def __str__(self):
                return self.numero_facture






