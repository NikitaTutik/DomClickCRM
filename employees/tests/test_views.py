from django.test import TestCase
from django.shortcuts import reverse


class EmployeePageTest(TestCase):

    def test_create_page(self):
        response = self.client.get(reverse("employees:employee-create"))
        self.assertEqual(response.status_code, 302)

    def test_update_page(self):
        response = self.client.get(reverse("employees:employees"))
        self.assertEqual(response.status_code, 302)

    def test_tickets_page(self):
        response = self.client.get(reverse("employees:employee_tickets"))
        self.assertEqual(response.status_code, 302)



