


from django.db import models
from django.contrib.auth.models import User

class emplyee(models.Model):
    username =models.CharField(max_length=20)
    paswword =models.CharField(max_length=20)
    email =models.CharField(max_length=20)
    role = models.CharField(max_length=20)
    def __str__(self):
        return self.username
