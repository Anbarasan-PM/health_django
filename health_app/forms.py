from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Data

class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = [
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
            'prediction'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

