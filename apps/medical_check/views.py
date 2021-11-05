# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from apps.medical_check.models import MedicalCheck
from apps.medical_check.serializers import MedicalCheckSerializer


class MedicalCheckModelViewSet(viewsets.ModelViewSet):
    serializer_class = MedicalCheckSerializer
    queryset = MedicalCheck.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'patient__id': ['exact']
    }
