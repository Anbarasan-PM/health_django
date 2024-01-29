from django.urls import path
from .views import login, otp_verification

app_name = 'auth'

urlpatterns = [
    path('login/', login, name='login'),
    path('otp-verification/', otp_verification, name='otp_verification'),
]
