from unittest import TestCase
from rest_framework.test import APIClient


class TestSome(TestCase):
    def test_some_view(self):
        url = '/api/v1/'
        client = APIClient()
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
