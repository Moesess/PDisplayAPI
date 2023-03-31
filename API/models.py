from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    last_modified = models.DateTimeField()

    class Meta:
        verbose_name = "Product"

    def __str__(self):
        return self.name


class PriceDisplay(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    ip_address = models.CharField(max_length=255)


