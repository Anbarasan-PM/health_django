import numpy as np
import hashlib
from django.core.validators import MinLengthValidator
from django.db import models
from django.core.exceptions import ValidationError
from sklearn.tree import DecisionTreeClassifier 
import joblib

GENDER=[
    (0,'Female'),
    (1,'Male')
]
FEVER = [
    (0,'Yes'),
    (1,'No')
]
COUGH = [
    (0,'Yes'),
    (1,'No')
]
FATIGUE = [
    (0,'Yes'),
    (1,'No')
]
DIFFICULTY_BREATHING = [
    (0,'Yes'),
    (1,'No')
]
BLOOD_PRESSURE=[
    (0,'Low'),
    (1,'Normal'),
    (2,'High')
]
CHOLESTROL_LEVEL=[
     (0,'Low'),
    (1,'Normal'),
    (2,'High')
]
AGE=[
   (0,'teen'), 
   (1,'youngester'),
   (2,'adult'),
   (3,'senior citizen')

]
DISEASE=[
(23,'Asthma'),
(16,'Stroke'),
(14,'Osteoporosis'),
(10,'Hypertension'),
(10,'Diabetes'),
(10,'Migraine'),
(8,'Influenza'),
(8,'Pneumonia'),
(8,'Bronchitis'),
(7,'Hyperthyroidism'),
(7,'Hypothyroidism'),
(6,'Rheumatoid Arthritis'),
(6,'Gastroenteritis'),
(6,'Anxiety Disorders'),
(6,'Allergic Rhinitis'),
(6,'Eczema'),
(6,'Common Cold'),
(6,'Depression'),
(6,'Liver Cancer'),
(6,'Kidney Cancer'),
(6,'Osteoarthritis'),
(5,'Coronary Artery Disease'),
(5,'Kidney Disease'),
(5,'Ulcerative Colitis'),
(5,'Pancreatitis'),
(5,'Psoriasis'),
(5,'Multiple Sclerosis'),
(5,'Urinary Tract Infection'),
(5,'Liver Disease'),
(5,'s Disease"'),
(4,'Chronic Obstructive Pulmonary Disease (COPD)'),
(3,'Hepatitis'),
(3,'Tuberculosis'),
(3,'Lung Cancer'),
(3,'Urinary Tract Infection (UTI)'),
(2,'Cholera'),
(2,'Rubella'),
(2,'Ebola Virus'),
(2,'Malaria'),
(2,'Dengue Fever'),
(2,'Mumps'),
(2,'Klinefelter Syndrome'),
(2,'Lyme Disease'),
(2,'Rabies'),
(2,'Turner Syndrome'),
(2,'Tetanus'),
(2,'Zika Virus'),
(2,'HIV/AIDS'),
(2,'Hemophilia'),
(2,'Measles'),
(2,'Chickenpox'),
(2,'Typhoid Fever'),
(2,'Hepatitis B'),
(1,'Others')
]
class Data(models.Model):
    Name=models.CharField(validators=[MinLengthValidator(2)],max_length=100,null=True)
    Disease	= models.PositiveIntegerField(choices=DISEASE,null=True)
    Fever	= models.PositiveIntegerField(choices=FEVER,null=True)
    Cough =  models.PositiveIntegerField(choices=COUGH,null=True)
    Fatigue	=  models.PositiveIntegerField(choices=FATIGUE,null=True)
    Difficult_Breathing =  models.PositiveIntegerField(choices=DIFFICULTY_BREATHING,null=True)	
    Gender	=  models.PositiveIntegerField(choices=GENDER,null=True)
    Blood_Pressure	=  models.PositiveIntegerField(choices=BLOOD_PRESSURE,null=True)
    Cholesterol_Level=  models.PositiveIntegerField(choices=CHOLESTROL_LEVEL,null=True)
    Age	= models.PositiveIntegerField(choices=AGE,null=True)
    prediction = models.PositiveIntegerField(blank=True,default=0)
    date = models.DateTimeField(auto_now_add=True)
  

    
    # Set the Python hash seed for reproducibility
    hash_seed = 42
    np.random.seed(hash_seed)
    
    def hash_function(self,data):
        # Using SHA-256 hash function
        sha256 = hashlib.sha256()
        sha256.update(str(data).encode())
        return int(sha256.hexdigest(), 16)
    
    def h_encrypt(self,value):
        # Map the hash value to a range between 1 and 100
        return 1 + (value % 100)
    
    def save(self, *args, **kwargs):
        ml_md = joblib.load('ml_health_classification/tree.joblib')
        
        # Hash and encrypt attributes
        hashed_disease = self.h_encrypt(self.hash_function(self.Disease))
        hashed_fever = self.h_encrypt(self.hash_function(self.Fever))
        hashed_cough = self.h_encrypt(self.hash_function(self.Cough))
        hashed_fatigue = self.h_encrypt(self.hash_function(self.Fatigue))
        hashed_difficult_breathing = self.h_encrypt(self.hash_function(self.Difficult_Breathing))
        hashed_gender = self.h_encrypt(self.hash_function(self.Gender))
        hashed_blood_pressure = self.h_encrypt(self.hash_function(self.Blood_Pressure))
        hashed_cholesterol_level = self.h_encrypt(self.hash_function(self.Cholesterol_Level))
        hashed_age = self.h_encrypt(self.hash_function(self.Age))
        
        # Predict
        self.prediction = ml_md.predict([[hashed_disease, hashed_fever, hashed_cough, hashed_fatigue, hashed_difficult_breathing, hashed_gender,
      hashed_blood_pressure, hashed_cholesterol_level, hashed_age]])
        
        # Save the instance with user-entered data
        return super().save(*args, **kwargs)



# Rest of your model class remains unchanged...


    class Meta:
        ordering=['-date']

    def __str__(self):
        return self.Name
    