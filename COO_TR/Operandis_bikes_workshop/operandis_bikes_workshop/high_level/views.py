# Create your views here.
import django
from django.views.generic import DetailView

from . import models


class PaysDetailView(DetailView):
    model = models.Pays

    def render_to_response(self, context, **response_kwargs):
        return django.http.JsonResponse(self.object.json())


class VilleDetailView(DetailView):
    model = models.Ville

    def render_to_response(self, context, **response_kwargs):
        return django.http.JsonResponse(self.object.json())


class ProduitDetailView(DetailView):
    model = models.Produit

    def render_to_response(self, context, **response_kwargs):
        return django.http.JsonResponse(self.object.json())


class QuantiteProduitDetailView(DetailView):
    model = models.QuantiteProduit

    def render_to_response(self, context, **response_kwargs):
        return django.http.JsonResponse(self.object.json())


class LieuDetailView(DetailView):
    model = models.Lieu

    def render_to_response(self, context, **response_kwargs):
        return django.http.JsonResponse(self.object.json())


class MachineDetailView(DetailView):
    model = models.Machine

    def render_to_response(self, context, **response_kwargs):
        return django.http.JsonResponse(self.object.json())


class QuantiteMachineDetailView(DetailView):
    model = models.Quantite_machine

    def render_to_response(self, context, **response_kwargs):
        return django.http.JsonResponse(self.object.json())


class TransportDetailView(DetailView):
    model = models.Transport

    def render_to_response(self, context, **response_kwargs):
        return django.http.JsonResponse(self.object.json())


class OperationDetailView(DetailView):
    model = models.Operation

    def render_to_response(self, context, **response_kwargs):
        return django.http.JsonResponse(self.object.json())


class PrixProduitDetailView(DetailView):
    model = models.Prix_Produit

    def render_to_response(self, context, **response_kwargs):
        return django.http.JsonResponse(self.object.json())


class FournisseurDetailView(DetailView):
    model = models.Fournisseur

    def render_to_response(self, context, **response_kwargs):
        return django.http.JsonResponse(self.object.json())


class StockDetailView(DetailView):
    model = models.Stock

    def render_to_response(self, context, **response_kwargs):
        return django.http.JsonResponse(self.object.json())


class PointDeVenteDetailView(DetailView):
    model = models.Point_de_vente

    def render_to_response(self, context, **response_kwargs):
        return django.http.JsonResponse(self.object.json())


class FactureDetailView(DetailView):
    model = models.Facture

    def render_to_response(self, context, **response_kwargs):
        return django.http.JsonResponse(self.object.json())
