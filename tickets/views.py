from django.shortcuts import reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Ticket, Employee
from .forms import TicketForm


class WelcomePageView(TemplateView):
    template_name = 'welcome_page.html'


class TicketListView(ListView):
    template_name = 'tickets/ticket_list.html'
    queryset = Ticket.objects.all()
    context_object_name = 'tickets'


class TicketDetailView(DetailView):
    template_name = 'tickets/ticket_detail.html'
    queryset = Ticket.objects.all()
    context_object_name = 'ticket'


class TicketCreateView(CreateView):
    template_name = 'tickets/ticket_create.html'
    form_class = TicketForm

    def get_success_url(self):
        return reverse('tickets:all-tickets')


class TicketUpdateView(UpdateView):
    template_name = 'tickets/ticket_update.html'
    queryset = Ticket.objects.all()
    form_class = TicketForm

    def get_success_url(self):
        return reverse('tickets:all-tickets')


class TicketDeleteView(DeleteView):
    template_name = 'tickets/ticket_delete.html'
    queryset = Ticket.objects.all()
    form_class = TicketForm

    def get_success_url(self):
        return reverse('tickets:all-tickets')



