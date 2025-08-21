from django.db import models

# Create your models here.

class Sale(models.Model):
    item_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.item_name} x{self.quantity} - {self.price}"
