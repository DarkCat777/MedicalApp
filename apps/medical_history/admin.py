from django.contrib import admin

# Register your models here.
from apps.medical_history.models import MedicalHistory

admin.site.register(MedicalHistory)
