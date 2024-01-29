# Generated by Django 5.0.1 on 2024-01-26 10:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_app', '0002_remove_data_result_alter_data_age_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='Age',
            field=models.PositiveIntegerField(choices=[(1, 'youngester'), (0, 'teen'), (3, 'senior citizen'), (2, 'adult')]),
        ),
        migrations.AlterField(
            model_name='data',
            name='Blood_Pressure',
            field=models.PositiveIntegerField(choices=[(0, 'Low'), (1, 'Normal'), (2, 'High')]),
        ),
        migrations.AlterField(
            model_name='data',
            name='Cholesterol_Level',
            field=models.PositiveIntegerField(choices=[(0, 'Low'), (1, 'Normal'), (2, 'High')]),
        ),
        migrations.AlterField(
            model_name='data',
            name='Disease',
            field=models.PositiveIntegerField(choices=[(6, 'Allergic Rhinitis'), (4, 'Chronic Obstructive Pulmonary Disease (COPD)'), (7, 'Hypothyroidism'), (3, 'Hepatitis'), (2, 'Hemophilia'), (5, 'Pancreatitis'), (2, 'Zika Virus'), (2, 'Rabies'), (5, 's Disease"'), (2, 'Malaria'), (6, 'Anxiety Disorders'), (5, 'Urinary Tract Infection'), (8, 'Pneumonia'), (10, 'Hypertension'), (2, 'Hepatitis B'), (6, 'Liver Cancer'), (2, 'Tetanus'), (3, 'Lung Cancer'), (2, 'Ebola Virus'), (2, 'Measles'), (6, 'Common Cold'), (3, 'Tuberculosis'), (2, 'Klinefelter Syndrome'), (5, 'Coronary Artery Disease'), (5, 'Multiple Sclerosis'), (2, 'Mumps'), (2, 'Lyme Disease'), (6, 'Kidney Cancer'), (2, 'Cholera'), (1, 'Others'), (6, 'Eczema'), (3, 'Urinary Tract Infection (UTI)'), (10, 'Migraine'), (6, 'Gastroenteritis'), (5, 'Ulcerative Colitis'), (23, 'Asthma'), (8, 'Influenza'), (14, 'Osteoporosis'), (6, 'Rheumatoid Arthritis'), (6, 'Osteoarthritis'), (8, 'Bronchitis'), (5, 'Psoriasis'), (2, 'Rubella'), (2, 'Turner Syndrome'), (5, 'Kidney Disease'), (2, 'HIV/AIDS'), (2, 'Typhoid Fever'), (6, 'Depression'), (7, 'Hyperthyroidism'), (10, 'Diabetes'), (5, 'Liver Disease'), (2, 'Dengue Fever'), (16, 'Stroke'), (2, 'Chickenpox')]),
        ),
        migrations.AlterField(
            model_name='data',
            name='Name',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
    ]
