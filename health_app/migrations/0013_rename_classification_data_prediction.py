# Generated by Django 5.0.1 on 2024-01-27 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health_app', '0012_alter_data_age_alter_data_blood_pressure_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='classification',
            new_name='prediction',
        ),
    ]