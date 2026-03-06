from django.db import models
from django.contrib.auth.models import User
from Denimapp.models import DenimItems


class CartItem(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(DenimItems, on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.product.denimPrice * self.quantity

    def __str__(self):
        return f"{self.user.username} - {self.product.denimName}"