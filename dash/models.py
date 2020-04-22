from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model

class Patient(models.Model):
    name = models.CharField("Imię", max_length=63)
    description = models.CharField("Opis", max_length=511)
    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name = 'Pacjent'
        verbose_name_plural = 'Pacjenci'

class Medication(models.Model):
    name = models.CharField("Nazwa", max_length=63)
    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name = 'Medykament'
        verbose_name_plural = 'Medykamenty'

class VisitType(models.Model):
    name = models.CharField("Nazwa", max_length=63)
    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name = 'Typ wizyty'
        verbose_name_plural = 'Typy wizyt'


class Visit(models.Model):
    title = models.CharField("Tytuł", max_length=63)
    description = models.CharField("Opis", max_length=1023)
    visit_type = models.ForeignKey(VisitType, on_delete=models.DO_NOTHING, verbose_name="Typ wizyty")
    date = models.DateTimeField("Data", blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING, verbose_name="Pacjent")
    wet = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING, verbose_name="Lekarz")

    class Meta:
        verbose_name = 'Wizyta'
        verbose_name_plural = 'Wizyty'

class MedicationDetailed(models.Model):
    medication = models.ForeignKey(Medication, on_delete=models.DO_NOTHING, verbose_name="Lek")
    dose = models.CharField("Dawkowanie", max_length=31)
    def __str__(self):
        return f"{self.medication}, {self.dose}"
    class Meta:
        verbose_name = 'Dawka Medykamentu'
        verbose_name_plural = 'Dawkowania Medykamentów'


class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING, verbose_name="Pacjent")
    medications = models.ManyToManyField(MedicationDetailed, verbose_name="Leki")
    created_at = models.DateTimeField("Data utworzenia", default=datetime.now)
    wet = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING, verbose_name="Lekarz")
    
    def __str__(self):
        return f"{self.patient}, {self.created_at}"
    class Meta:
        verbose_name = 'Recepta'
        verbose_name_plural = 'Recepty'

