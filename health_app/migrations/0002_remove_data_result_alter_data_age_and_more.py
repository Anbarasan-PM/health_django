# Generated by Django 5.0.1 on 2024-01-26 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='Result',
        ),
        migrations.AlterField(
            model_name='data',
            name='Age',
            field=models.PositiveIntegerField(choices=[(1, 'youngester'), (3, 'senior citizen'), (0, 'teen'), (2, 'adult')]),
        ),
        migrations.AlterField(
            model_name='data',
            name='Blood_Pressure',
            field=models.PositiveIntegerField(choices=[(0, 'Low'), (2, 'High'), (1, 'Normal')]),
        ),
        migrations.AlterField(
            model_name='data',
            name='Cholesterol_Level',
            field=models.PositiveIntegerField(choices=[(0, 'Low'), (2, 'High'), (1, 'Normal')]),
        ),
        migrations.AlterField(
            model_name='data',
            name='Cough',
            field=models.PositiveIntegerField(choices=[(0, 'Yes'), (1, 'No')]),
        ),
        migrations.AlterField(
            model_name='data',
            name='Difficult_Breathing',
            field=models.PositiveIntegerField(choices=[(0, 'Yes'), (1, 'No')]),
        ),
        migrations.AlterField(
            model_name='data',
            name='Disease',
            field=models.PositiveIntegerField(choices=[(5, 'Coronary Artery Disease'), (2, 'Hemophilia'), (8, 'Influenza'), (7, 'Hyperthyroidism'), (6, 'Depression'), (8, 'Bronchitis'), (4, 'Chronic Obstructive Pulmonary Disease (COPD)'), (2, 'Rubella'), (2, 'Cholera'), (8, 'Pneumonia'), (2, 'Zika Virus'), (10, 'Hypertension'), (3, 'Urinary Tract Infection (UTI)'), (6, 'Common Cold'), (2, 'Turner Syndrome'), (3, 'Tuberculosis'), (2, 'Chickenpox'), (23, 'Asthma'), (6, 'Anxiety Disorders'), (5, 'Kidney Disease'), (10, 'Migraine'), (6, 'Kidney Cancer'), (5, 'Multiple Sclerosis'), (2, 'Klinefelter Syndrome'), (2, 'Lyme Disease'), (1, 'Others'), (5, 'Ulcerative Colitis'), (3, 'Hepatitis'), (2, 'Malaria'), (6, 'Liver Cancer'), (2, 'HIV/AIDS'), (10, 'Diabetes'), (3, 'Lung Cancer'), (5, 's Disease"'), (6, 'Eczema'), (6, 'Osteoarthritis'), (5, 'Pancreatitis'), (6, 'Rheumatoid Arthritis'), (2, 'Mumps'), (2, 'Rabies'), (6, 'Gastroenteritis'), (14, 'Osteoporosis'), (5, 'Liver Disease'), (2, 'Tetanus'), (7, 'Hypothyroidism'), (6, 'Allergic Rhinitis'), (5, 'Psoriasis'), (2, 'Ebola Virus'), (2, 'Measles'), (2, 'Typhoid Fever'), (5, 'Urinary Tract Infection'), (2, 'Dengue Fever'), (16, 'Stroke'), (2, 'Hepatitis B')]),
        ),
        migrations.AlterField(
            model_name='data',
            name='Fatigue',
            field=models.PositiveIntegerField(choices=[(0, 'Yes'), (1, 'No')]),
        ),
        migrations.AlterField(
            model_name='data',
            name='Fever',
            field=models.PositiveIntegerField(choices=[(0, 'Yes'), (1, 'No')]),
        ),
        migrations.AlterField(
            model_name='data',
            name='Gender',
            field=models.PositiveIntegerField(choices=[(1, 'Male'), (0, 'Female')]),
        ),
    ]