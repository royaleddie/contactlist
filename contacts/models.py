from django.db import models

# Create your models here.

class Contact(models.Model):
    full_name = models.CharField(max_length=500)
    relationship = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    
    