# authentication/models.py
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Add any additional fields or methods you need
    pass
