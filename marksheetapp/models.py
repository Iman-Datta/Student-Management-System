from django.db import models
from studentapp.models import Student
from subjectapp.models import Subject

class Marksheet(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.IntegerField()
    max_marks = models.IntegerField(default=100)
    exam_name = models.CharField(max_length=100, blank=True, null=True)
    percentage = models.FloatField(editable=False, default=0)

    class Meta:
        unique_together = ('student', 'subject', 'exam_name')

    def save(self, *args, **kwargs):
        if self.max_marks:
            self.percentage = (self.marks / self.max_marks) * 100
        else:
            self.percentage = 0
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student} - {self.subject}: {self.marks}/{self.max_marks} ({self.percentage:.2f}%)"
