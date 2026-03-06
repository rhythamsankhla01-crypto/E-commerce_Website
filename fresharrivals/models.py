from django.db import models

# Create your models here.

class freshArrivals(models.Model):
    freshImage = models.ImageField(upload_to='fresh_arrivals/', null=True, blank=True);
    freshTitle = models.CharField(max_length=100);
    freshMrp = models.IntegerField();
    freshPrice = models.IntegerField();
    freshOffer = models.IntegerField();
    freshbestprice = models.IntegerField();
    

    def __str__(self):
        return self.freshTitle  # To show meaningful names instead of boring object IDs.

    class Meta:
        verbose_name_plural = "Fresh Arrivals"