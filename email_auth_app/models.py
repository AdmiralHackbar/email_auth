from django.db import models
from datetime import datetime

class Token(models.Model):
    username = models.CharField(max_length=30)
    token = models.CharField(max_length=50, primary_key=True)