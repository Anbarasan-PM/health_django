from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Data
from .forms import DataForm

@login_required(login_url='login')  # Requires the user to be logged in to access the view
def home(request):
    if request.user.is_authenticated:
        # User is authenticated, you can customize this part as needed
        return render(request, 'health_app/index.html', {'username': request.user.username})
    else:
        # User is not authenticated, render the login form or redirect to the login page
        return render(request, 'login.html')  # You may need to create a 'login.html' template

def index(request):
    if request.method == "POST":
        form = DataForm(request.POST)
        if form.is_valid():
            data_instance = form.save(commit=False)
            data_instance.user = request.user  # Assign the logged-in user to the data instance
            data_instance.save()
            messages.success(request, 'Data submitted successfully!')
            return redirect('health_app-prediction')
    else:
        form = DataForm()

    context = {
        'form': form,
    }
    return render(request, 'health_app/index.html', context)



def prediction(request):
    prediction = Data.objects.all()
    encrypt = []

    for data in prediction:
        encrypt.append({
            'Disease': data.h_encrypt(data.hash_function(data.Disease)),
            'Fever': data.h_encrypt(data.hash_function(data.Fever)),
            'Cough': data.h_encrypt(data.hash_function(data.Cough)),
            'Fatigue': data.h_encrypt(data.hash_function(data.Fatigue)),
            'Difficult_Breathing': data.h_encrypt(data.hash_function(data.Difficult_Breathing)),
            'Gender': data.h_encrypt(data.hash_function(data.Gender)),
            'Blood_Pressure': data.h_encrypt(data.hash_function(data.Blood_Pressure)),
            'Cholesterol_Level': data.h_encrypt(data.hash_function(data.Cholesterol_Level)),
            'Age': data.h_encrypt(data.hash_function(data.Age)),
        })

    zipp = zip(prediction, encrypt)

    context = {
        'zipp': zipp,
    }

    return render(request, 'health_app/prediction.html', context)