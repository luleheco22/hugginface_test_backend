from django.db import models

# Create your models here.
class Users(models.Model):
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
