from django.db import models
from django.utils import timezone


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product_id = models.CharField(max_length=255, default="NONE")
    last_modified = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["name", "-last_modified"]
        get_latest_by = ["name", "-last_modified"]
        verbose_name = "Product"

    def save(self, *args, **kwargs):
        self.product_id = "PROD_" + str(self.name).upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class PriceDisplay(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    ip_address = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)


