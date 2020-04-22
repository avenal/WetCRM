from django.db import models
from datetime import datetime

class Patient(models.Model):
    name = models.CharField(max_length=63)
    description = models.CharField(max_length=511)
    def __str__(self):
        return f"{self.name}"

class Medication(models.Model):
    name = models.CharField(max_length=63)
    def __str__(self):
        return f"{self.name}"

class VisitType(models.Model):
    name = models.CharField(max_length=63)
    def __str__(self):
        return f"{self.name}"

class Visit(models.Model):
    title = models.CharField(max_length=63)
    description = models.CharField(max_length=1023)
    visit_type = models.ForeignKey(VisitType, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)

class MedicationDetailed(models.Model):
    mediacation = models.ForeignKey(Medication, on_delete=models.DO_NOTHING)
    dose = models.CharField(max_length=31)
    def __str__(self):
        return f"{self.name}, {self.dose}"

class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    medications = models.ManyToManyField(MedicationDetailed)
    created_at = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return f"{self.patient}, {self.created_at}"
