from django.db import models


class Car(models.Model):
    type = models.CharField(max_length=16)
    name = models.CharField(max_length=32)
    url = models.CharField(max_length=128)

    class Meta:
        db_table = "car"
