from django.db import models
import datetime

# Create your models here.
#This is for the costumer
class Contact(models.Model):  # Renamed to avoid conflict with Django's built-in User model
    full_name = models.CharField(max_length=50)
    email_address = models.EmailField()
    phone_number = models.CharField(max_length=50, blank=True, null=True)  # Use PhoneNumberField from django-phonenumber-field
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    is_finished = models.BooleanField(default=False) 
    def __str__(self):
        return self.full_name

