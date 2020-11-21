from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from ..models.patient import Patient
from ..serializers import PatientSerializer

# Create your views here.
class Patients(APIView):
    def get(self, request):
        """Index Request"""
        print(request.session)
        patients = Patient.objects.all()[:10]
        data = PatientSerializer(patients, many=True).data
        return Response(data)

    serializer_class = PatientSerializer
    def post(self, request):
        """Post request"""
        print(request.data)
        patient = PatientSerializer(data=request.data['patient'])
        if patient.is_valid():
            b = patient.save()
            return Response(patient.data, status=status.HTTP_201_CREATED)
        else:
            return Response(patient.errors, status=status.HTTP_400_BAD_REQUEST)

class PatientDetail(APIView):
    def get(self, request, pk):
        """Show request"""
        patient = get_object_or_404(Patient, pk=pk)
        data = PatientSerializer(patient).data
        return Response(data)

    def patch(self, request, pk):
        """Update Request"""
        patient = get_object_or_404(Patient, pk=pk)
        ms = PatientSerializer(patient, data=request.data['patient'])
        if ms.is_valid():
            ms.save()
            return Response(ms.data)
        return Response(ms.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Delete Request"""
        patient = get_object_or_404(Patient, pk=pk)
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
