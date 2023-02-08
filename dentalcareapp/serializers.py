from rest_framework import serializers
from .models import Dentist, Patient, Appointment

class DentistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dentist
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'phone',
            'years_of_experience',
            'practice_location',
            'image',
        )


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = (
            'id',
            'first_name',
            'last_name',
            'age',
            'date_of_birth',
            'email',
            'phone',
            'address',
            'postal_code',
            'dentist',
            'image',
        )


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = (
            'id',
            'name',
            'date_time',
            'dentist',
            'patient',
            'location',
        )