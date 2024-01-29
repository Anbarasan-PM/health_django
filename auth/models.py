from django.db import models

class UserProfile(models.Model):
    class Meta:
        app_label='auth'
    phone_number = models.CharField(max_length=10)
    otp = models.CharField(max_length=6)
