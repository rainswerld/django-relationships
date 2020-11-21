from django.urls import path

from .views.patient_views import Patients, PatientDetail
from .views.doctor_views import Doctors, DoctorDetail

urlpatterns = [
    path('doctors', Doctors.as_view(), name='doctors'),
    path('doctors/<int:pk>', DoctorDetail.as_view(), name='author_detail'),
    path('patients', Patients.as_view(), name='patients'),
    path('patients/<int:pk>', PatientDetail.as_view(), name='patient_detail'),
]
