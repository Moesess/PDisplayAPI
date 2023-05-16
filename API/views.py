from django.urls import reverse
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Product, PriceDisplay, ProductChange
from.serializers import ProductSerializer, PriceDisplaySerializer, ProductChangeSerializer


class ProductListView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class PriceDisplayListView(viewsets.ModelViewSet):
    queryset = PriceDisplay.objects.all()
    serializer_class = PriceDisplaySerializer

    @action(detail=True, methods=['get'])
    def get_qr_code_img_url(self, request, pk=None):
        instance = self.get_object()
        qr_code_img_url = request.build_absolute_uri(reverse('pricedisplay-detail', args=[instance.uid]))

        response_data = {
            "uid": instance.uid,
            "qr_code_img_url": qr_code_img_url,
            "qr_code": instance.qr_code,
            "created_at": instance.created_at,
            "modified_at": instance.modified_at,
            "product": instance.product.pk
        }

        return Response(response_data)


class ProductChangeView(viewsets.ModelViewSet):
    queryset = ProductChange.objects.all()
    serializer_class = ProductChangeSerializer
