from rest_framework import serializers

from apps.medical_check.serializers import MedicalCheckSerializer
from apps.medical_history.models import MedicalHistory
from apps.patient.serializers import PatientSerializer


class MedicalHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalHistory
        fields = '__all__'


class MedicalHistoryDetailSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(many=False)
    medical_check = MedicalCheckSerializer(many=False)

    class Meta:
        model = MedicalHistory
        fields = '__all__'
