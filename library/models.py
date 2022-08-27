from email.policy import default
from random import choices
from django.db import models


# Create your models here.

class Book(models.Model):
    status = (
        ('BORROWED', 'BORROWED'),
        ("AVAILABLE", 'AVAILABLE')
    )
    title = models.CharField(max_length=255)
    status = models.CharField(choices=status, max_length=20, default="AVAILABLE")
    author = models.CharField(max_length=255)
