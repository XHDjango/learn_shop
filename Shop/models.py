from django.db import models


# Create your models here.

class Shop(models.Model):
    nid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    img_url = models.CharField(max_length=256)

    class Meta:
        db_table = "shop"