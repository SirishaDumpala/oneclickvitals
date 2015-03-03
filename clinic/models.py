from django.db import models
from django.utils import timezone


class Appointment(models.Model):
    author = models.ForeignKey('auth.User')
    patient_first_name = models.CharField(max_length=15, null = True)
    patient_last_name = models.CharField(max_length=15, null = True)
    patient_phone_number = models.CharField(max_length=10, null = True)
    #patient_name = models.CharField(max_length=15)
    #phone_numer = models.PhoneNumberField()
    reason = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    appointment_date = models.DateTimeField(
            blank=True, null=True)

    def confirm_appointment(self): #function for confirming appointment
        self.appointment_date = timezone.now()
        self.save()

    def __str__(self):
        return self.patient_last_name

class Prescription(models.Model):
    author = models.ForeignKey('auth.User')
    patient_first_name = models.CharField(max_length=15, null = True)
    patient_last_name = models.CharField(max_length=15, null = True)
    pharmacy_phone_number = models.CharField(max_length=10, null = True)
    #patient_name = models.CharField(max_length=15)
    #phone_numer = models.PhoneNumberField()
    medicine_name = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)

    def confirm_prescription(self): #function for confirming prescrption
        self.prescription_date = timezone.now()
        self.save()

    def __str__(self):

        return self.patient_last_name

