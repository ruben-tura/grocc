from django.db import models

# Create your models here.
class Order(models.Model):
    title = models.CharField(max_length=100)

class Entry(models.Model):
    orderID = models.ForeignKey(to="Order", on_delete=models.CASCADE)
    article = models.CharField(max_length=100)
    quantity = models.IntegerField()
    colour = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=7 ,decimal_places=2)