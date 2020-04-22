from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Patient)
admin.site.register(Medication)
admin.site.register(VisitType)
admin.site.register(MedicationDetailed)
admin.site.register(Prescription)
admin.site.register(Visit)