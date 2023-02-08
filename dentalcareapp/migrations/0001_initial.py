# Generated by Django 4.1.5 on 2023-01-22 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dentist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('years_of_experience', models.IntegerField()),
                ('practice_location', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('dentist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dentalcareapp.dentist')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('date_time', models.DateTimeField()),
                ('location', models.CharField(max_length=50)),
                ('dentist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dentalcareapp.dentist')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dentalcareapp.patient')),
            ],
        ),
    ]