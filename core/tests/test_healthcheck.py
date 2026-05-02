from django.test import TestCase
from django.urls import reverse


class HealthcheckTest(TestCase):
    def test_healthcheck_returns_ok(self):
        response = self.client.get("/health/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok"})

    def test_healthcheck_returns_json(self):
        response = self.client.get("/health/")
        self.assertEqual(response["Content-Type"], "application/json")
