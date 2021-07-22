from django.test import TestCase
from django.shortcuts import reverse


class WelcomePageTest(TestCase):

    def test_welcome_page(self):
        response = self.client.get(reverse("welcome_page"))
        self.assertEqual(response.status_code, 200)

    def test_template_welcome(self):
        response = self.client.get(reverse("welcome_page"))
        self.assertTemplateUsed(response, "welcome_page.html")
