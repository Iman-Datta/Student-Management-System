from django.db import models

# This model.py file is used to create a class representation of a TABLE
# This class will be converted in RDBMS table with the help of
# 2 commands
# 'makemigrations' that would create an intermediate file (000_initial.py)
# 'migrate' that will create the table from the intermediate file

class Student(models.Model):
    name = models.CharField(max_length=100)
    maths = models.IntegerField()
    chemistry =  models.IntegerField()
    physics =  models.IntegerField()
    total = models.IntegerField()

    def save(self, *args, **kwargs ):
        self.total = self.maths+self.chemistry+self.physics
        return super().save(*args, **kwargs)