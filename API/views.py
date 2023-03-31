from rest_framework import viewsets, mixins

from .models import Product, PriceDisplay
from.serializers import ProductSerializer, PriceDisplaySerializer


class ProductListView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class PriceDisplayListView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = PriceDisplay.objects.all()
    serializer_class = PriceDisplaySerializer
