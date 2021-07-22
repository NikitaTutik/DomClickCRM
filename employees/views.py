from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse
from tickets.models import Employee
from .forms import EmployeeForm
from .mixins import ManagerAndLoginReqMixin


class EmployeeView(ManagerAndLoginReqMixin, generic.ListView):
    template_name = "employees/employee_list.html"

    def get_queryset(self):
        company = self.request.user.employee.company
        return Employee.objects.filter(company=company)


class EmployeeCreateView(ManagerAndLoginReqMixin, generic.CreateView):
    template_name = "employees/employee_create.html"
    form_class = EmployeeForm

    def get_success_url(self):
        return reverse("employees:employees")

    def form_valid(self, form):
        employee = form.save(commit=False)
        employee.company = self.request.user.employee.company
        employee.save()
        return super(EmployeeCreateView, self).form_valid(form)


class EmployeeDetail(ManagerAndLoginReqMixin, generic.DetailView):
    template_name = 'employees/employee_detail.html'
    context_object_name = 'employee'

    def get_queryset(self):
        return reverse("employees:employees")


class EmployeeUpdate(ManagerAndLoginReqMixin, generic.UpdateView):
    template_name = "employees/employee_update.html"
    form_class = EmployeeForm

    def get_success_url(self):
        return reverse("employees:employees")



