from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Auctions(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True)