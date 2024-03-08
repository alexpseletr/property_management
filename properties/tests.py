from django.urls import reverse
from rest_framework.test import APITestCase
from .models import Property
from unittest.mock import patch
import json

false = False
class PropertyTests(APITestCase):
    def setUp(self):
        self.property_data = {
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

    def test_create_property(self):
        self.url = reverse('property-retrieve-update-destroy', kwargs={'id': self.property.id})
        expected_url = f'/api/properties/{self.property.id}/'
        self.assertEqual(self.url, expected_url)

    def test_get_property(self):
        response = self.client.get(reverse('property-list-create'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.property_data['property_code'])

    @patch('django.urls.reverse')
    def test_update_property(self, mock_reverse):
        mock_reverse.return_value = '/api/properties/1/'
        updated_property_data = {
            "property_code": "PRO200",
            "guest_limit": 6,
            "bathroom_count": 3,
            "pets_allowed": True,
            "cleaning_fee": "70.00",
            "activation_date": "2024-03-08",
            "created_at": "2024-03-07T12:07:19.702Z",
            "updated_at": "2024-03-07T12:07:19.702Z"
        }
        json_data = json.dumps(updated_property_data)
        response = self.client.put('/api/properties/1/', data=json_data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['property_code'], updated_property_data['property_code'])

    @patch('django.urls.reverse')
    def test_get_individual_property(self, mock_reverse):
        mock_reverse.return_value = '/api/properties/1/'
        response = self.client.get('/api/properties/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['property_code'], self.property_data['property_code'])

    @patch('django.urls.reverse')
    def test_get_nonexistent_property(self, mock_reverse):
        mock_reverse.return_value = '/api/properties/1000/'
        response = self.client.get('/api/properties/1000/')
        self.assertEqual(response.status_code, 404)
        
    @patch('django.urls.reverse')
    def test_delete_property(self, mock_reverse):
        mock_reverse.return_value = '/api/properties/1/'
        response = self.client.delete('/api/properties/1/')
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Property.objects.filter(id=self.property.id).exists())
