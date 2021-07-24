from django.test import TestCase
from tickets.models import Ticket, Employee, Category
from django.contrib.auth import get_user_model

User = get_user_model()


class ModelTest(TestCase):

    def test_ticket_model(self):
        self.name = Ticket.objects.create(name='testuser')
        self.date = Ticket.objects.create(date='07122021')
        self.details = Ticket.objects.create(details='some details')
        self.urgent = Ticket.objects.create(urgent=True)
        self.assertEqual(str(self.name), "testuser")

    def test_category_model(self):
        self.name = Category.objects.create(name='Open')
        self.assertEqual(str(self.name), "Open")



