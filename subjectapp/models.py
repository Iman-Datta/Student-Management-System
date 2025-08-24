from django.db import models
from streamapp.models import Stream

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True) # name is public access specifier
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE)
    
    # get(): Search
    def __str__(self):
        return f"Subject name: {self.name} - Stream name: {self.stream.name}"