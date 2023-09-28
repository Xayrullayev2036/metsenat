from django.db import models
from core.models import TimeSteppedModel
from sponsor.models import Sponsor
from students.choices import EducationType


class Institute(models.Model):
    name = models.CharField(max_length=125)


class Student(TimeSteppedModel):
    fullname = models.CharField(max_length=125)
    student_type = models.CharField(max_length=100, choices=EducationType.choices)
    institute = models.ForeignKey(Institute, related_name="student_institute", on_delete=models.PROTECT,blank=True)
    contract_amount = models.FloatField()

    class Meta:
        verbose_name = "Students"
        verbose_name_plural = "Students"

    def __str__(self):
        return f"{self.fullname}"


class StudentSponsor(TimeSteppedModel):
    sponsor = models.ForeignKey(Sponsor, related_name='sponsor', on_delete=models.PROTECT)
    student = models.ForeignKey(Student, related_name='student', on_delete=models.PROTECT)
    allocated_amount = models.FloatField()