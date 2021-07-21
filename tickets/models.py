from django.db import models


class Ticket(models.Model):
    name = models.CharField(max_length=256)
    details = models.CharField(max_length=1000)
    category = models.CharField(max_length=10)

