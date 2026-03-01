from django.db import models

class Poloitems(models.Model):
    poloImage = models.ImageField();
    poloName = models.CharField(max_length=100);
    poloPrice = models.IntegerField();
    poloMrp = models.IntegerField();
    poloOffer = models.IntegerField();
    poloBestprice = models.IntegerField();
# Create your models here.
