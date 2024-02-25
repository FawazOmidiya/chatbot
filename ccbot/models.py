from django.db import models
from datetime import datetime

# Create your models here.

class User(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    DOB = models.DateField("Date of Birth")