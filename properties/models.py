from django.db import models

class Property(models.Model):
    property_code = models.CharField(max_length=100, unique=True)
    guest_limit = models.PositiveIntegerField()
    bathroom_count = models.PositiveIntegerField()
    pets_allowed = models.BooleanField()
    cleaning_fee = models.DecimalField(max_digits=10, decimal_places=2)
    activation_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
