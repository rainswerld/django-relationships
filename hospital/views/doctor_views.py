from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from ..models.doctor import Doctor
from ..serializers import DoctorSerializer

# Create your views here.
class Doctors(APIView):
    def get(self, request):
        """Index Request"""
        print(request.session)
        doctors = Doctor.objects.all()[:10]
        data = DoctorSerializer(doctors, many=True).data
        return Response(data)

    serializer_class = DoctorSerializer
    def post(self, request):
        """Post request"""
        print(request.data)
        doctor = DoctorSerializer(data=request.data['doctor'])
        if doctor.is_valid():
            b = doctor.save()
            return Response(doctor.data, status=status.HTTP_201_CREATED)
        else:
            return Response(doctor.errors, status=status.HTTP_400_BAD_REQUEST)

class DoctorDetail(APIView):
    def get(self, request, pk):
        """Show request"""
        doctor = get_object_or_404(Doctor, pk=pk)
        data = DoctorSerializer(doctor).data
        return Response(data)

    def patch(self, request, pk):
        """Update Request"""
        doctor = get_object_or_404(Doctor, pk=pk)
        ms = DoctorSerializer(doctor, data=request.data['doctor'])
        if ms.is_valid():
            ms.save()
            return Response(ms.data)
        return Response(ms.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Delete Request"""
        doctor = get_object_or_404(Doctor, pk=pk)
        doctor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
