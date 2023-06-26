from django.db import models

class customer(models.Model):
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    role = models.CharField(max_length=10)
    password = models.CharField(max_length=30,default="password@123")
    last_login = models.DateTimeField(auto_now=True)
    