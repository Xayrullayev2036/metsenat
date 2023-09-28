from celery import shared_task
import logging

from sponsor.models import Sponsor
from students.models import StudentSponsor

logger = logging.getLogger("sponsors")


# @shared_task
# def send_students_info():
#     sponsors = Sponsor.objects.all()
#     for sponsor in sponsors:
#         print(f"Sponsor: {sponsor.fullname}")
#         print(StudentSponsor.objects.filter(sponsor=sponsor).values("student"))
#
#
# @shared_task
# def send_status_info():
#     sponsors = Sponsor.objects.all()
#     for sponsor in sponsors:
#         if sponsor.status == "yangi":
#             print(f"{sponsor.fullname}")
