from django.db import models
import decimal

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
    size = models.CharField(max_length=20, blank=True, default='M')
    additional_notes = models.CharField(max_length=200, blank=True, default='')
    quantity = models.IntegerField(default=1)
    colour = models.CharField(max_length=20, blank=True, default='nero')
    price = models.DecimalField(max_digits=7 ,decimal_places=2)
    total_price = models.DecimalField(max_digits=7 ,decimal_places=2, blank=True, default=0)
    discounted_price = models.DecimalField(max_digits=7 ,decimal_places=2, blank=True, default=0)

    def save(self, *args, **kwargs):
        self.total_price = self.price * self.quantity
        self.discounted_price = self.total_price * decimal.Decimal('0.90')
        super(Entry, self).save(*args, **kwargs)

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ', ' + self.article