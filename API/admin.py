from django.contrib import admin

from .models import Product, PriceDisplay


class ProductAdmin(admin.ModelAdmin):
    model = Product

    list_display = ["name", "price", "product_id", "last_modified"]


class PriceDisplayAdmin(admin.ModelAdmin):
    model = PriceDisplay

    list_display = [field.name for field in PriceDisplay._meta.get_fields()]


admin.site.register(Product, ProductAdmin)
admin.site.register(PriceDisplay, PriceDisplayAdmin)
