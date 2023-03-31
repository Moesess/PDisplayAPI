from rest_framework import serializers

from .models import Product, PriceDisplay


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class PriceDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceDisplay
        fields = '__all__'
