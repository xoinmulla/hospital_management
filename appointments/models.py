from django.db import models
from patients.models import Patient
from doctors.models import Doctor

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.patient.name} with {self.doctor.name} on {self.appointment_date}"
