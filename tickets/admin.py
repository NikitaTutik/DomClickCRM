from django.contrib import admin
from .models import Ticket, Employee, User


admin.site.register(Ticket)
admin.site.register(Employee)
admin.site.register(User)