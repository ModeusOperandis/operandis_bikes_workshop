from django.db import models


# Create your models here.
class Pays(models.Model):
    nom = models.CharField()
    tva = models.FloatField()
    tarif_electrique = models.FloatField()
    salaire_minimum = models.FloatField()

    def __str__(self):
        return self.nom

    def json(self):
        return {
            "nom": self.nom,
            "tva": self.tva,
            "tarif_electrique": self.tarif_electrique,
            "salaire_minimum": self.salaire_minimum,
        }


class Ville(models.Model):
    nom = models.CharField()
    taxe_immobiliere = models.CharField()
    prix_metre_carre = models.FloatField()
    pays = models.ForeignKey(Pays, on_delete=models.PROTECT)

    def __str__(self):
        return self.nom

    def json(self):
        return {
            "nom": self.nom,
            "taxe_immobiliere": self.taxe_immobiliere,
            "pays": self.pays,
        }


class Produit(models.Model):
    nom = models.CharField()
    prix_de_vente = models.FloatField(blank=True, null=True)
    duree_de_vie = models.FloatField()
    nombre_par_palette = models.IntegerField()
    operation = models.ForeignKey(
        "Operation", blank=True, null=True, on_delete=models.PROTECT
    )  # c'est une liste chaînée

    def __str__(self):
        return self.nom

    def json(self):
        return {
            "nom": self.nom,
            "prix_de_vente": self.prix_de_vente,
            "duree_de_vie": self.duree_de_vie,
            "nombre_par_palette": self.nombre_par_palette,
            "operation": self.operation,
        }

    def costs(self):
        somme = self.prix_de_vente
        op = self.operation
        while op.operation_suivante:
            somme = somme + self.operation.costs()
            op = op.operation_suivante

        return somme


class QuantiteProduit(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.PROTECT)
    nombre = models.IntegerField()

    def __str__(self):
        return self.produit.nom + "->" + self.nombre

    def json(self):
        return {"produit": self.produit, "nombre": self.nombre}


class Lieu(models.Model):
    nom = models.CharField()
    ville = models.ManyToManyField("Ville")
    superficie = models.FloatField()
    quantite_machines = models.ForeignKey("Quantite_machine", on_delete=models.PROTECT)
    consomation_electrique = models.FloatField()

    def __str__(self):
        return self.nom

    def costs(self):
        return (
            (self.superficie * self.ville.prix_metre_carre)
            + (self.consomation_electrique * self.ville.pays.tarif_electrique)
            + (self.quantite_machines * self.quantite_machines.type_machine.costs())
        )

    def json(self):
        return {
            "nom": self.nom,
            "ville": self.ville,
            "superficie": self.superficie,
            "quantite_machines": self.quantite_machines,
            "consomation_electrique": self.consomation_electrique,
        }


class Machine(models.Model):
    nom = models.CharField()
    prix = models.FloatField()
    duree_de_vie = models.FloatField()
    cout_de_maintenance = models.FloatField()
    superficie = models.FloatField()

    def __str__(self):
        return self.nom

    def costs(self):
        return self.prix + (self.cout_de_maintenance * self.duree_de_vie)

    def json(self):
        return {
            "nom": self.nom,
            "prix": self.prix,
            "duree_de_vie": self.duree_de_vie,
            "cout_de_maintenance": self.cout_de_maintenance,
            "superficie": self.superficie,
        }


class Quantite_machine(models.Model):
    type_machine = models.ForeignKey(
        Machine, blank=True, null=True, on_delete=models.PROTECT
    )
    nombre = models.IntegerField()

    def json(self):
        return {"type_machine": self.type_machine, "nombre": self.nombre}


class Transport(models.Model):
    nombre_palettes = models.IntegerField()
    cout = models.FloatField()
    delai = models.FloatField()
    depart = models.ForeignKey(Lieu, on_delete=models.PROTECT, related_name="depart+")
    arrive = models.ForeignKey(Lieu, on_delete=models.PROTECT)

    def json(self):
        return {
            "nombre_palettes": self.nombre_palettes,
            "cout": self.cout,
            "delai": self.delai,
            "depart": self.depart,
            "arrive": self.arrive,
        }


class Operation(models.Model):
    nom = models.CharField(max_length=100)
    operation_suivante = models.ForeignKey(
        "self", blank=True, null=True, on_delete=models.PROTECT
    )  # liste chaînée
    cout = models.FloatField()
    machine = models.ForeignKey(Machine, on_delete=models.PROTECT)
    quantite_produit = models.ManyToManyField("QuantiteProduit", blank=True, null=True)
    heure_de_travail = models.FloatField()
    consomation_electrique = models.FloatField()

    def __str__(self):
        return self.nom

    def costs(self):
        return (
            self.cout
            + self.heure_de_travail
            * (
                self.machine.quantite_machine_set.first()
                .lieu_set.first()
                .ville.pays.salaire_minimum
            )
            + self.consomation_electrique
            * (
                self.machine.quantite_machine_set.first()
                .lieu_set.first()
                .ville.pays.tarif_electrique
            )
        )

    def json(self):
        return {
            "nom": self.nom,
            "operation_suivante": self.operation_suivante,
            "cout": self.cout,
            "machine": self.machine,
            "quantite_produit": self.quantite_produit,
            "heure_de_travail": self.heure_de_travail,
            "consomation_electrique": self.consomation_electrique,
        }


class Prix_Produit(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.PROTECT)
    prix_achat = models.FloatField()

    def json(self):
        return {"produit": self.produit, "prix_achat": self.prix_achat}


class Fournisseur(models.Model):
    nom = models.CharField()
    produit = models.ManyToManyField(Produit)
    prix_achat = models.FloatField()

    def json(self):
        return {"nom": self.nom, "produit": self.produit, "prix_achat": self.prix_achat}

    def __str__(self):
        return self.nom


class Stock(models.Model):
    quantite_produit = models.ManyToManyField("QuantiteProduit")
    palettes_max = models.IntegerField()

    def costs(self):
        return self.quantite_produit.nombre * self.quantite_produit.produit.costs()

    def json(self):
        return {
            "quantite_produit": self.quantite_produit,
            "palettes_max": self.palettes_max,
        }


class Point_de_vente(models.Model):
    nom = models.CharField()
    lieu = models.ForeignKey(Lieu, on_delete=models.PROTECT)
    heure_de_travail = models.FloatField()
    stock = models.ForeignKey(Stock, on_delete=models.PROTECT)

    def __str__(self):
        return self.nom

    def costs(self):
        return self.stock.costs + self.lieu.costs()

    def json(self):
        return {
            "nom": self.nom,
            "lieu": self.lieu,
            "heure_de_travail": self.heure_de_travail,
            "stock": self.stock,
        }


class Facture(models.Model):
    numero_facture = models.CharField(max_length=100)
    quantite_produit = models.ManyToManyField("QuantiteProduit")
    reduction = models.FloatField()
    point_de_vente = models.ForeignKey(Point_de_vente, on_delete=models.PROTECT)
    client = models.CharField()

    def __str__(self):
        return self.numero_facture

    def json(self):
        return {
            "numero_facture": self.numero_facture,
            "quantite_produit": self.quantite_produit,
            "reduction": self.reduction,
            "point_de_vente": self.point_de_vente,
            "client": self.client,
        }
