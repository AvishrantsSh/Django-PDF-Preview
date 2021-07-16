from django.db import models
from django.db.models.base import Model


class StudentRecord(models.Model):
    name = models.CharField(help_text="Name of Student", max_length=50, blank=False)
    roll_no = models.IntegerField()
    score = models.IntegerField()

    def __str__(self) -> str:
        return self.name
