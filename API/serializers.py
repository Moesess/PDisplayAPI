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
    # product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    product_details = serializers.SerializerMethodField()

    class Meta:
        model = PriceDisplay
        fields = ('uid', 'qr_code_img', 'product_details', 'qr_code', 'created_at', 'modified_at')

    def get_product_details(self, obj):
        serializer = ProductSerializer(obj.product)
        return serializer.data
