from django.contrib import admin

from .models import Product, PriceDisplay


class ProductAdmin(admin.ModelAdmin):
    model = Product

    list_display = ('id', 'name', 'price', 'last_modified')


class PriceDisplayAdmin(admin.ModelAdmin):
    model = PriceDisplay

    list_display = ('id', 'ip_address')


admin.site.register(Product, ProductAdmin)
admin.site.register(PriceDisplay, PriceDisplayAdmin)
