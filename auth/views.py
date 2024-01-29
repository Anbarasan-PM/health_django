import random
import phonenumbers
from phonenumbers import carrier
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm
from .models import UserProfile

def generate_otp():
    # Generate a random 6-digit OTP
    return str(random.randint(100000, 999999))

def send_otp(phone_number, otp):
    # In a real-world scenario, you would integrate with an SMS gateway to send the OTP
    print(f'Sending OTP {otp} to {phone_number}')

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            aadhar_number = form.cleaned_data['aadhar_number']
            phone_number = form.cleaned_data['phone_number']

            # Generate OTP
            otp = generate_otp()

            # Send OTP to the user's phone number
            send_otp(phone_number, otp)

            # Store OTP in the database
            user_profile, created = UserProfile.objects.get_or_create(
                aadhar_number=aadhar_number,
                phone_number=phone_number
            )
            user_profile.otp = otp
            user_profile.save()

            return redirect('auth:otp_verification')
    else:
        form = LoginForm()

    return render(request, 'auth/login.html', {'form': form})

def otp_verification(request):
    if request.method == "POST":
        entered_otp = request.POST.get('otp')
        phone_number = request.POST.get('phone_number')

        # Retrieve user profile
        user_profile = UserProfile.objects.filter(phone_number=phone_number).first()

        if user_profile and user_profile.otp == entered_otp:
            messages.success(request, 'Login Successful!')
            return redirect('health_app-index')
        else:
            messages.error(request, 'Invalid OTP. Please try again.')

    return render(request, 'auth/otp_verification.html')
