from celery import shared_task
import logging

from students.models import Student
from students.models import StudentSponsor


logger = logging.getLogger("students")


@shared_task
def student_amount_filter():
    students = Student.objects.all()
    student_allocated_amount = StudentSponsor.objects.all()
    for student in students:
        for amount in student_allocated_amount:
            if student.contract_amount >= amount.allocated_amount:
                print(student.fullname)


