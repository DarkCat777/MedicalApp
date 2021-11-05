from rest_framework import serializers

from apps.medical_check.serializers import MedicalCheckSerializer
from apps.medical_history.models import MedicalHistory
from apps.patient.serializers import PatientSerializer


class MedicalHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalHistory
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.patient:
            data['patient'] = PatientSerializer(instance.patient, context=self.context).data
        if instance.medical_check:
            data['medical_check'] = MedicalCheckSerializer(instance.medical_check, context=self.context).data
        return data
