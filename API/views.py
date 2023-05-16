from rest_framework import viewsets, mixins

from .models import Product, PriceDisplay, ProductChange
from.serializers import ProductSerializer, PriceDisplaySerializer, ProductChangeSerializer


class ProductListView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class PriceDisplayListView(viewsets.ModelViewSet):
    queryset = PriceDisplay.objects.all()
    serializer_class = PriceDisplaySerializer


class ProductChangeView(viewsets.ModelViewSet):
    queryset = ProductChange.objects.all()
    serializer_class = ProductChangeSerializer
