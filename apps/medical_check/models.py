from django.db import models

# Create your models here.
from apps.patient.models import Patient


class MedicalCheck(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    weight = models.FloatField(blank=False, null=False)
    temperature = models.FloatField(blank=False, null=False)
    pressure = models.FloatField(blank=False, null=False)
    saturation = models.FloatField(blank=False, null=False)

    def __str__(self):
        return f'{type(self).__name__}({", ".join("%s=%s" % item for item in vars(self).items() if item[0][0] != "_")})'
