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
    Product.objects.update_or_create(
        id=1,
        name='Banana',
        price='1.23',
        last_modified=datetime.datetime.now()
    )

    Product.objects.update_or_create(
        id=2,
        name='Orange',
        price='2.34',
        last_modified=datetime.datetime.now()
    )

    Product.objects.update_or_create(
        id=3,
        name='Corn',
        price='3.45',
        last_modified=datetime.datetime.now()
    )

    Product.objects.update_or_create(
        id=4,
        name='Milk',
        price='4.56',
        last_modified=datetime.datetime.now()
    )

    PriceDisplay.objects.update_or_create(
        id=1,
        ip_address='127.0.0.2'
    )

    PriceDisplay.objects.update_or_create(
        id=2,
        ip_address='127.0.0.3'
    )

    PriceDisplay.objects.update_or_create(
        id=3,
        ip_address='127.0.0.4'
    )

    return HttpResponse("Objects created")

