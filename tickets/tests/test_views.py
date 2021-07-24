from django.test import TestCase
from django.shortcuts import reverse


class WelcomePageTest(TestCase):

    def test_welcome_page(self):
        response = self.client.get(reverse("welcome_page"))
        self.assertEqual(response.status_code, 200)

    def test_template_welcome(self):
        response = self.client.get(reverse("welcome_page"))
        self.assertTemplateUsed(response, "welcome_page.html")


class IdentificationPageTest(TestCase):

    def test_register_page(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)

    def test_template_signup(self):
        response = self.client.get(reverse("signup"))
        self.assertTemplateUsed(response, "registration/sign_up.html")

    def test_login_page(self):
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)

    def test_template_login(self):
        response = self.client.get(reverse("login"))
        self.assertTemplateUsed(response, "registration/login.html")


