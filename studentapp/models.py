from django.db import models

# This model.py file is used to create a class representation of a TABLE
# This class will be converted in RDBMS table with the help of
# 2 commands
# 'makemigrations' that would create an intermediate file (000_initial.py)
# 'migrate' that will create the table from the intermediate file

class Stream(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)


