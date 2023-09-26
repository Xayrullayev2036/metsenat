from django.db import models


class EducationType(models.TextChoices):
    BACHELORS = ("bachelors", "Bachelors")
    MASTER = ("master", "Master")

