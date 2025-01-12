
import unittest
from app import create_app

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_main_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_api_route(self):
        response = self.client.get('/api/data')
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.get_json())
