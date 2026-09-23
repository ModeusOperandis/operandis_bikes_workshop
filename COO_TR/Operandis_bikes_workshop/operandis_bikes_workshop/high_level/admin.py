from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Pays)
admin.site.register(models.Ville)
admin.site.register(models.Point_de_vente)
admin.site.register(models.Operation)
admin.site.register(models.Stock)
admin.site.register(models.Machine)
admin.site.register(models.Facture)
admin.site.register(models.Lieu)
admin.site.register(models.Quantite_machine)
admin.site.register(models.Transport)
admin.site.register(models.Produit)
admin.site.register(models.Prix_Produit)
admin.site.register(models.QuantiteProduit)