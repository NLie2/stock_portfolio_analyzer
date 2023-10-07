from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  year_born = models.IntegerField(blank=True, null=True)