# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from apps.medical_history.models import MedicalHistory
from apps.medical_history.serializers import MedicalHistorySerializer


class MedicalHistoryModelViewSet(viewsets.ModelViewSet):
    serializer_class = MedicalHistorySerializer
    queryset = MedicalHistory.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'patient__id': ['exact']
    }
