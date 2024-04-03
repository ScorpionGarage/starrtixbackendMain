from django.contrib.auth.models import AbstractUser, User
from django.db import models

class CustomUser(AbstractUser):
    phonenumber = models.CharField(max_length=20, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)






