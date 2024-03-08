from django.urls import reverse
from rest_framework.test import APITestCase
from .models import Adverts
from unittest.mock import patch, MagicMock
from properties.models import Property

class AdvertsTests(APITestCase):
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
        self.url = reverse('advert-retrieve-update', kwargs={'id':1})

    def test_retrieve_advert(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['property_id'], self.advert_data['property_id'].id)

    @patch('django.urls.reverse')
    @patch('adverts.models.Adverts.objects.get')
    def test_get_individual_advert(self, mock_get_advert, mock_reverse):
        mock_reverse.return_value = '/api/adverts/1/'
        mock_property_instance = MagicMock(spec=Property)
        mock_property_instance.id = self.property.id
        mock_get_advert.return_value = self.advert
        response = self.client.get('/api/adverts/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['property_id'], mock_property_instance.id)

    @patch('django.urls.reverse')
    def test_get_nonexistent_advert(self, mock_reverse):
        mock_reverse.return_value = '/api/adverts/1000/'
        response = self.client.get('/api/adverts/1000/')
        self.assertEqual(response.status_code, 404)
    
    def test_delete_advert(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, 405)
