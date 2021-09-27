from rest_framework import serializers

from apps.medical_check.models import MedicalCheck


class MedicalCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalCheck
        fields = '__all__'
