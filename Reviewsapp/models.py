from django.db import models

# Create your models here.
class Reviews(models.Model):
    PersonName = models.CharField(max_length=25);
    Description = models.CharField(max_length=50);