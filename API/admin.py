from django.contrib import admin

from .models import Product, PriceDisplay, ProductChange


class ProductAdmin(admin.ModelAdmin):
    model = Product

    list_display = ["uid", "name", "price", "modified_at", "created_at"]


class PriceDisplayAdmin(admin.ModelAdmin):
    model = PriceDisplay

    list_display = [field.name for field in model._meta.get_fields()]


admin.site.register(Product, ProductAdmin)
admin.site.register(PriceDisplay, PriceDisplayAdmin)
