from django.db import models

class Tshirt(models.Model):
    tshirtImage = models.ImageField();
    tshirtName = models.CharField(max_length=100);
    tshirtPrice = models.IntegerField();
    tshirtMrp = models.IntegerField();
    tshirtOffer = models.IntegerField();
    tshirtBestprice = models.IntegerField();


    def __str__(self):
        return self.tshirtName  # To show meaningful names instead of boring object IDs.

    class Meta:
        verbose_name_plural = "TopWear"
# Create your models here.
