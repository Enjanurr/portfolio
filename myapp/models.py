from django.db import models


# Create your models here.

class Contact(models.Model):  # Renamed to avoid conflict with Django's built-in User model
    full_name = models.CharField(max_length=50)
    email_address = models.EmailField()
    phone_number = models.CharField(max_length=50, blank=True, null=True)  # Use PhoneNumberField from django-phonenumber-field
    message = models.TextField()

    def __str__(self):
        return self.full_name

# This model is for the comment
'''class Comment(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comment {self.body[:20]} by {self.name}'  # Display a truncated version of the body

'''