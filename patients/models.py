from django.db import models

# Create your models here.

class Add_patients(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    image = models.ImageField(upload_to='images/')


    def __str__(self):
        return self.name