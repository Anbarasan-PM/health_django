# authentication/views.py
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from .forms import CustomAuthenticationForm  # Correct the import statement

class CustomLoginView(LoginView):
    template_name = 'authentication/login.html'
    authentication_form = CustomAuthenticationForm

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home')

class ProfileView(TemplateView):
    template_name = 'authentication/profile.html'
