from django.contrib import admin

# Register your models here.
from apps.patient.models import Patient

admin.site.register(Patient)
