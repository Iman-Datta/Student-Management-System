from django.db import models
from streamapp.models import Stream
from . utils import generate_roll_number

class Student(models.Model):
    # Personal info:
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)    
    # date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField()

    # Guardian Info
    guardian_name = models.CharField(max_length=100)
    guardian_relation = models.CharField(max_length=50)  # Father, Mother, Uncle, etc.
    guardian_contact = models.CharField(max_length=15)

    # Contact info:
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    # Educatoinal info:
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE)
    roll_number = models.CharField(max_length=20, unique=True)
    section = models.CharField(max_length=10)


    def save(self, *args, **kwargs):
        new_rollNum = generate_roll_number()
        while Student.objects.filter(roll_number = new_rollNum).exists():
            new_rollNum = generate_roll_number()
        self.roll_number = new_rollNum
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.name} ({self.roll_number})"