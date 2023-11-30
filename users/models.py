from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Department(models.Model):
    department = models.CharField(max_length=100)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField
    date_of_birth = models.DateField()
    email = models.EmailField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name
