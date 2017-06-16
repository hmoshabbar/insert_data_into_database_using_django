from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Users(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name=models.CharField(max_length=230)
    email=models.EmailField(max_length=200)
    salary=models.CharField(max_length=15)
    phone=models.CharField(max_length=200)
    address=models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
