# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response

from apps.medical_history.models import MedicalHistory
from apps.medical_history.serializers import MedicalHistorySerializer, MedicalHistoryDetailSerializer


class MedicalHistoryModelViewSet(viewsets.ModelViewSet):
    serializer_class = MedicalHistorySerializer
    queryset = MedicalHistory.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = MedicalHistoryDetailSerializer(instance)
        return Response(serializer.data)
