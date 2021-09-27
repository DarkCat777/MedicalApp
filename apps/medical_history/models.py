from django.db import models

# Create your models here.
from apps.medical_check.models import MedicalCheck
from apps.patient.models import Patient


class MedicalHistory(models.Model):
    date_of_check = models.DateField(blank=False, null=False, auto_now=False, auto_created=False, auto_now_add=False)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medical_check = models.ForeignKey(MedicalCheck, on_delete=models.CASCADE)

    def __str__(self):
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s=%s' % item for item in vars(self).items() if item[0][0] != '_')
        )
