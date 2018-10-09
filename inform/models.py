from django.db import models


class Shop(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    road_address = models.CharField(max_length=100)
    mapX = models.CharField(max_length=20)
    mapY = models.CharField(max_length=20)
