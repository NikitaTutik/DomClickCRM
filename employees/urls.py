from django.urls import path
from .views import EmployeeView, EmployeeCreateView, EmployeeDetail, EmployeeUpdate, EmployeeTickets

app_name = "employees"

urlpatterns = [
    path('', EmployeeView.as_view(), name='employees'),
    path('create/', EmployeeCreateView.as_view(), name='employee-create'),
    path('<int:pk>/', EmployeeDetail.as_view(), name='employee_detail'),
    path('<int:pk>/update/', EmployeeUpdate.as_view(), name='employee_update'),
    path('mytickets/', EmployeeTickets.as_view(), name='employee_tickets')
]