import uuid
from django.db import models

# Create your models here.

class Appointments(models.Model):
    patient_name = models.CharField(max_length=20)
    doctors_name = models.CharField(max_length=225)
    special_id = models.CharField(max_length=32, default=uuid.uuid4().hex[:5], editable=False, unique=True)
    time_slot = models.CharField(max_length=20)
    department = models.CharField(max_length=20)
    appointment_date = models.CharField(max_length=22)
    token_number = models.CharField(max_length=32)
    problem = models.TextField(max_length=225)

    def __str__(self):
        return self.doctors_name