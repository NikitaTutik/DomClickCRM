from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_manager = models.BooleanField(default=True)
    is_supermanager = models.BooleanField(default=False)


class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')

    def __str__(self):
        return self.user.username


class Ticket(models.Model):
    name = models.CharField(max_length=256)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    details = models.CharField(max_length=1000)
    urgent = models.BooleanField(default=False)
    company = models.ForeignKey(ProfileModel,null=True, blank=True, on_delete=models.CASCADE)
    employee = models.ForeignKey("Employee", null=True, blank=True, on_delete=models.SET_NULL)
    category = models.ForeignKey("Category",null=True, blank=True, on_delete=models.SET_NULL)
    status = models.ForeignKey("Status", null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(ProfileModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


def post_user_signal(sender, instance, created, **kwargs):
    if created:
        ProfileModel.objects.create(user=instance)


post_save.connect(post_user_signal, sender=User)






