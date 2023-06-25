from django.db import models
from django.contrib.auth.models import User
class YourModel(models.Model):
    # Existing fields
    username = models.CharField(max_length=100)
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    # New field
    role = models.CharField(max_length=100)

