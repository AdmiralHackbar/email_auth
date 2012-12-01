from django.db import models

# Create your models here.
class AuthUser(models.Model):
    email = models.CharField(max_length=200)
