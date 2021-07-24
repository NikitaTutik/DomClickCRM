from django.test import TestCase
from tickets.forms import TicketForm
from django.contrib.auth import get_user_model
from tickets.models import Ticket, Category, Employee, Status

User = get_user_model()


class TestForms(TestCase):

    def test_ticket_form_valid(self):
        form = TicketForm(data={
            'name': Ticket.objects.create(name='somename'),
            'details': Ticket.objects.create(details='details'),
            'category': Category.objects.create(name='DB'),
            'urgent': Ticket.objects.create(urgent=True),
            'employee': Employee.objects.create(user=User.objects.create(username='test',password='password'), company_id='1'),
            'status': Status.objects.create(name='Open'),
        })
        self.assertFalse(form.is_valid())
