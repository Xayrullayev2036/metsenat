from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import TimeSteppedModel
from sponsor.choices import SponsorTypeChoices, StatusChoices, PaymentTypeChoices


class Sponsor(TimeSteppedModel):
    fullname = models.CharField(_("fullname"), max_length=150, blank=True)
    sponsor_type = models.CharField(max_length=125, choices=SponsorTypeChoices.choices, blank=True)
    phone_number = models.CharField(max_length=13, unique=True, blank=True)
    status = models.CharField(max_length=50, choices=StatusChoices.choices, blank=True)
    company_name = models.CharField(max_length=100, null=True)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, default=0)
    payment_type = models.CharField(max_length=125, choices=PaymentTypeChoices.choices)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        verbose_name = "Sponsor"
        verbose_name_plural = "Sponsor"

    def get_full_name(self):
        full_name = f"{self.fullname}"
        return full_name

