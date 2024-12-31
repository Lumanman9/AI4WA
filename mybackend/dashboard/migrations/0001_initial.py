# Generated by Django 4.2.17 on 2024-12-31 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PatientTracking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(blank=True, help_text='Description of the patient', null=True)),
                ('count', models.IntegerField(default=0, help_text='Number of times the patient currently in the waiting room')),
            ],
        ),
        migrations.CreateModel(
            name='ImageData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='images/')),
                ('patient_tracking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.patienttracking')),
            ],
        ),
    ]