from django.db import models

class FootwearItems(models.Model):
    footwearImage = models.ImageField();
    footwearName = models.CharField(max_length=100);
    footwearPrice = models.IntegerField();
    footwearMrp = models.IntegerField();
    footwearOffer = models.IntegerField();
    footwearBestprice = models.IntegerField();

# Create your models here.
