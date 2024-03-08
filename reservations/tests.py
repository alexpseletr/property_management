from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Reservation
from .models import Adverts
from properties.models import Property


class ReservationTests(APITestCase):
    def setUp(self):
        self.property_data = {
            "id": 1,
            "property_code": "PRO100",
            "guest_limit": 4,
            "bathroom_count": 2,
            "pets_allowed": False,
            "cleaning_fee": "50.00",
            "activation_date": "2024-03-07",
            "created_at": "2024-03-07T12:07:19.702Z",
            "updated_at": "2024-03-07T12:07:19.702Z"
        }
        self.property = Property.objects.create(**self.property_data)
        self.advert_data = {
            "property_id": self.property,
            "platform_name": "AirBnb",
            "platform_fee": 10.00
        }
        self.advert = Adverts.objects.create(**self.advert_data)
        self.reservation_data = {
            "adverts_id": self.advert,
            "total_price": "200.00",
            "comment": "A wonderful stay!",
            "guest_count": 2,
            "check_in_date": "2024-03-15",
            "check_out_date": "2024-03-20"
        }
        self.reservation = Reservation.objects.create(**self.reservation_data)
        self.url = reverse('reservation-retrieve-update-destroy', kwargs={'reservation_id': self.reservation.reservation_id})

    def test_create_reservation(self):
        reservation_data = {"adverts_id": 1, "check_in_date": "2024-03-15", "check_out_date": "2024-03-20", "total_price": 200.00, "comment": "A wonderful stay!", "guest_count": 2}
        response = self.client.post(reverse('reservation-list-create'), data=reservation_data)
        self.assertEqual(response.status_code, 201)

    def test_create_reservation_with_invalid_dates(self):
        reservation_data = {
            "adverts_id": 1,
            "check_in_date": "2024-03-20",
            "check_out_date": "2024-03-15",
            "total_price": 200.00,
            "comment": "A wonderful stay!",
            "guest_count": 2
        }
        response = self.client.post(reverse('reservation-list-create'), data=reservation_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_retrieve_reservation(self):
        self.url = reverse('reservation-retrieve-update-destroy', kwargs={'reservation_id': self.reservation.reservation_id})
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['reservation_id'], self.reservation.reservation_id)

    def test_delete_reservation(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, 204)
    
    def test_update_reservation(self):
        updated_data = {
            "check_in_date": "2024-03-16",
            "check_out_date": "2024-03-21",
            "total_price": "250.00",
            "comment": "Another wonderful stay!",
            "guest_count": 3
        }
        response = self.client.put(self.url, data=updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
