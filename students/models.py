from django.db import models

from core.models import HeadModel
from students.choices import EducationType


class Institute(models.Model):
    name = models.CharField(max_length=125)


class Student(HeadModel):
    fullname = models.CharField(max_length=125)
    student_type = models.CharField(max_length=100, choices=EducationType.choices)
    institute = models.ForeignKey(Institute, related_name="student_institute", on_delete=models.CASCADE)
    contract_amount = models.FloatField()

    class Meta:
        verbose_name = "Students"
        verbose_name_plural = "Students"

    def __str__(self):
        return f"{self.fullname}"
