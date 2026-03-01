from django.db import models

class DenimItems(models.Model):
    denimImage = models.ImageField();
    denimName = models.CharField(max_length=100);
    denimPrice = models.IntegerField();
    denimMrp = models.IntegerField();
    denimOffer = models.IntegerField();
    denimBestprice = models.IntegerField();

# Create your models here.
