# Create your views here.
from rest_framework import viewsets

from apps.patient.models import Patient
from apps.patient.serializers import PatientSerializer


class PatientModelViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()
