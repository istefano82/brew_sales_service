import json
from unittest import mock

from rest_framework.test import APITestCase


class BrewAuthApiUnittest(APITestCase):
    """Test complete integration between views, serailizers and models"""

    def setUp(self):
        self.sale1_data = {
            'title': 'Beer Light',
            'sales_amount': 1000,
            'sales_person': 'Bob'
        }
        self.sale2_data = {
            'title': 'Beer Dark',
            'sales_amount': 500,
            'sales_person': 'Jane'
        }

    @mock.patch("brew_sales.views.requests", autospec=True)
    def test_get_total_sales_amount(self, mock_requests):
        """It should be possible to get total sales amount"""
        base_url = '/api/v0/brew_sales/sales_item/'
        response = self.client.get(base_url + 'total_sales/')
        self.assertEqual({'total_sales': 0}, json.loads(response.content))
        self.client.post(base_url, data=self.sale1_data, format='json')
        response = self.client.get(base_url + 'total_sales/')
        self.assertEqual({'total_sales': 1000}, json.loads(response.content))
        self.client.post(base_url, data=self.sale2_data, format='json')
        response = self.client.get(base_url + 'total_sales/')
        self.assertEqual({'total_sales': 1500}, json.loads(response.content))
