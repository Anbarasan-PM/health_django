from django import forms

class LoginForm(forms.Form):
    aadhar_number = forms.CharField(max_length=12)
    phone_number = forms.CharField(max_length=10)
