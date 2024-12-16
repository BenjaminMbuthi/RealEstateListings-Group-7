
# Create your tests here.
from rest_framework.test import APITestCase
from .models import Agent

class AgentTestCase(APITestCase):
    def test_create_agent(self):
        data = {'name': 'John Doe', 'email': 'john@example.com', 'phone_number': '1234567890'}
        response = self.client.post('/api/agents/', data)
        self.assertEqual(response.status_code, 201)
