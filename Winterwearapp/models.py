from django.db import models

class Winterwearitems(models.Model):
    winterwearImage = models.ImageField(upload_to='winterwear/');
    winterwearName = models.CharField(max_length=100);
    winterwearPrice = models.IntegerField();
    winterwearMrp = models.IntegerField();
    winterwearOffer = models.IntegerField();
    winterwearBestprice = models.IntegerField();

# Create your models here.
