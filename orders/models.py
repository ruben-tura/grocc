from django.db import models

# Create your models here.
class Order(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Entry(models.Model):
    orderID = models.ForeignKey(to="Order", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    club = models.CharField(max_length=100)
    article = models.CharField(max_length=100)
    size = models.CharField(max_length=20)
    additional_notes = models.CharField(max_length=200)
    quantity = models.IntegerField()
    colour = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=7 ,decimal_places=2)
    total_price = models.DecimalField(max_digits=7 ,decimal_places=2, blank=True, default=0)
    discounted_price = models.DecimalField(max_digits=7 ,decimal_places=2, blank=True, default=0)

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ', ' + self.article