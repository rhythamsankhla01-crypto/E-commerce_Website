from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from Denimapp.models import DenimItems


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    product = GenericForeignKey('content_type', 'object_id')

    quantity = models.IntegerField(default=1)

    def subtotal(self):
        return self.product.denimPrice * self.quantity

    def __str__(self):
        return f"{self.user.username} - {self.product.denimName}"
# Create your models here.



