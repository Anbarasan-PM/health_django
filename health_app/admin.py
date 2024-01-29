from django.contrib import admin
from .models import Data

class DataAdmin(admin.ModelAdmin):
    list_display = (
        'Name',
        'Disease',
        'Fever',
        'Cough',
        'Fatigue',
        'Difficult_Breathing',
        'Gender',
        'Blood_Pressure',
        'Cholesterol_Level',
        'Age',
        'prediction',
        'date',
    )

admin.site.register(Data, DataAdmin)
