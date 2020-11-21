from rest_framework import serializers

from .models.doctor import Doctor
from .models.patient import Patient

class DoctorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Doctor
    fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
  class Meta:
    model = Patient
    fields = '__all__'
