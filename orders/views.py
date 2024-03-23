from django.shortcuts import render
from .models import Order, Entry

# Create your views here.
def orders(request):
    orders = Order.objects.all()
    entries = Entry.objects.all()
    return render(request, 'orders.html', context={'orders': orders, 'entries': entries})