from django.contrib import admin
from .models import Ticket, Employee, User, ProfileModel, Category


admin.site.register(Category)
admin.site.register(ProfileModel)
admin.site.register(Ticket)
admin.site.register(Employee)
admin.site.register(User)