from django.db import models

# Create your models here.

class Doctors(models.Model):
    name = models.CharField(max_length=200)
    specialization = models.CharField(max_length=225)
    age = models.IntegerField()
    email = models.EmailField()
    details = models.TextField(max_length=225)
    date_of_birth = models.DateField()
    experience = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=225)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name