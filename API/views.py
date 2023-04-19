import datetime

from django.http import HttpResponse

from rest_framework import viewsets, mixins

from .models import Product, PriceDisplay
from.serializers import ProductSerializer, PriceDisplaySerializer


class ProductListView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class PriceDisplayListView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = PriceDisplay.objects.all()
    serializer_class = PriceDisplaySerializer


def get_products(request):
    Product.objects.create(
        name='Banana',
        price='1.23',
    )

    Product.objects.create(
        name='Orange',
        price='2.34',
    )

    Product.objects.create(
        name='Corn',
        price='3.45',
    )

    Product.objects.create(
        name='Milk',
        price='4.56',
    )

    # PriceDisplay.objects.update_or_create(
    #     id=1,
    #     ip_address='127.0.0.2'
    # )
    #
    # PriceDisplay.objects.update_or_create(
    #     id=2,
    #     ip_address='127.0.0.3'
    # )
    #
    # PriceDisplay.objects.update_or_create(
    #     id=3,
    #     ip_address='127.0.0.4'
    # )

    return HttpResponse("Objects created")


def get_latest_product(request):
    return HttpResponse(Product.objects.filter(name__contains="milk").latest().last_modified)
