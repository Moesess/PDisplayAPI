from django.contrib import admin

from .models import Product, PriceDisplay, ProductChange


class ProductAdmin(admin.ModelAdmin):
    model = Product

    list_display = [field.name for field in Product._meta.get_fields()]


class PriceDisplayAdmin(admin.ModelAdmin):
    model = PriceDisplay

    list_display = [field.name for field in PriceDisplay._meta.get_fields()]


class ProductChangeAdmin(admin.ModelAdmin):
    model = ProductChange

    list_display = [field.name for field in ProductChange._meta.get_fields()]


admin.site.register(Product, ProductAdmin)
admin.site.register(PriceDisplay, PriceDisplayAdmin)
admin.site.register(ProductChange, ProductChangeAdmin)
