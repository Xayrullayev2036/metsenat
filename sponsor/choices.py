from django.db import models


class SponsorTypeChoices(models.TextChoices):
    YURIDIK = ["yuridik", "Yuridik"]
    JISMONIY = ["jismoniy", "Jismoniy"]


class StatusChoices(models.TextChoices):
    YANGI = ["yangi", "Yangi"]
    MODERATSIYADA = ["moderatsiyada", "Moderatsiyada"]
    TASDIQLANGAN = ["Tasdiqlangan", "Tasdiqlangan"]
    BEKOR_QILINGAN = ["bekor qilingan", "Bekor qilingan"]


class PaymentTypeChoices(models.TextChoices):
    NAQD = ["naqd", "Naqd"]
    KARTA = ["karta", "Karta"]
