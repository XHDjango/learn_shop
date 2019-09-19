from django.db import models


# Create your models here.

class Shop(models.Model):
    nid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    img_url = models.CharField(max_length=256)

    class Meta:
        db_table = "shop"

class Car(models.Model):
    type = models.CharField(max_length=16)
    name = models.CharField(max_length=32)
    url = models.CharField(max_length=128)

    class Meta:
        db_table = "car"