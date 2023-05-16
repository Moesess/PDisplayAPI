import uuid

from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from PDisplayAPI.settings import WEBSITE_URL


class Product(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name", "-modified_at"]
        get_latest_by = ["name", "-modified_at"]
        verbose_name = "Product"

    def __str__(self):
        return self.name


class ProductChange(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    name = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)


@receiver(post_save, sender=Product)  # after Product object is saved, create ProductChange object
def create_product_change(sender, instance, created, **kwargs):
    ProductChange.objects.create(
        name=instance.name,
        product=instance,
        price=instance.price,
        timestamp=instance.modified_at
    )


class PriceDisplay(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qr_code = models.CharField(max_length=500, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


@receiver(pre_save, sender=PriceDisplay)  # create qr_code as url with uid of PriceDisplay before object is saved
def generate_qr_code(sender, instance, **kwargs):
    instance.qr_code = f"{WEBSITE_URL}/PriceDisplay/{instance.uid}"
