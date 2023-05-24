from django.db import models

# Create your models here.

class UsersMessages(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    message = models.TextField()

