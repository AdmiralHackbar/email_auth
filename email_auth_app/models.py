from django.db import models

class AuthUser(models.Model):
    email = models.CharField(max_length=300, primary_key=True)
    name = models.CharField(max_length=200)

class AuthToken(models.Model):
    authUser = models.ForeignKey(AuthUser)
    token = models.CharField(max_length=50, primary_key=True)
    timestamp = models.TimeField(auto_now_add=True)
