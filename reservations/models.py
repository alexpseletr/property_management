from django.db import models
from django.utils.crypto import get_random_string
from adverts.models import Adverts

class Reservation(models.Model):
    reservation_id = models.CharField(max_length=100, primary_key=True)
    adverts_id = models.ForeignKey(Adverts, on_delete=models.CASCADE, related_name='reservations')
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.TextField(blank=True)
    guest_count = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.reservation_id:
            self.reservation_id = get_random_string(length=10)  # Gera um ID de reserva aleatório
        super().save(*args, **kwargs)
