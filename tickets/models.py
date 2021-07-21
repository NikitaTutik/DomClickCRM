from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Ticket(models.Model):
    name = models.CharField(max_length=256)
    details = models.CharField(max_length=1000)
    category = models.CharField(max_length=10)
    urgent = models.BooleanField(default=False)
    employee = models.ForeignKey("Employee", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email




