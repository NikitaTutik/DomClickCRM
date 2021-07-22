from django.shortcuts import reverse
from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Ticket, Employee
from .forms import TicketForm, UserRegisterForm


class SignUpView(CreateView):
    template_name = "registration/sign_up.html"
    form_class = UserRegisterForm

    def get_success_url(self):
        return reverse('login')


class WelcomePageView(TemplateView):
    template_name = 'welcome_page.html'


class TicketListView(LoginRequiredMixin, ListView):
    template_name = 'tickets/ticket_list.html'
    context_object_name = 'tickets'

    def get_queryset(self):
        if self.request.user.is_manager:
            queryset = Ticket.objects.filter(employee__isnull=False)
        else:
            queryset = Ticket.objects.filter(company=self.request.user.employee.company)
        queryset = queryset.filter(employee__user=self.request.user)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TicketListView, self).get_context_data(**kwargs)
        if self.request.user.is_manager:
            queryset = Ticket.objects.filter(employee__isnull=True)
            context.update({
                "unassigned_tickets":queryset
            })
        return context


class TicketDetailView(LoginRequiredMixin, DetailView):
    template_name = 'tickets/ticket_detail.html'
    queryset = Ticket.objects.all()
    context_object_name = 'ticket'


class TicketCreateView(LoginRequiredMixin, CreateView):
    template_name = 'tickets/ticket_create.html'
    form_class = TicketForm

    def get_success_url(self):
        return reverse('tickets:all-tickets')

    def form_valid(self, form):
        send_mail(
            subject="New ticket has been created and assigned to an employee.",
            message="Review new ticket at ##",
            from_email="test@testdomclick.ru",
            recipient_list=["employee@testdomclick.ru"]
         )
        return super(TicketCreateView, self).form_valid(form)


class TicketUpdateView(LoginRequiredMixin, UpdateView):
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



