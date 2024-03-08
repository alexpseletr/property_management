from django.db import models
from properties.models import Property

class Adverts(models.Model):
    property_id = models.ForeignKey(Property, on_delete=models.CASCADE)
    platform_name = models.CharField(max_length=100)
    platform_fee = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
