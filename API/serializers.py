from rest_framework import serializers

from .models import Product, ProductChange, PriceDisplay


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductChange
        fields = '__all__'


class PriceDisplaySerializer(serializers.ModelSerializer):
    qr_code_img = serializers.ImageField(use_url=True, read_only=True)
    product = ProductSerializer()

    class Meta:
        model = PriceDisplay
        fields = '__all__'
