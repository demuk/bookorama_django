from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    user_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    bio = models.TextField((""))
    last_seen = models.DateTimeField((""), auto_now=False, auto_now_add=True)
