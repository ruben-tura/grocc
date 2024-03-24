from django.shortcuts import render
from .models import Order, Entry
from .forms import OrderForm, EntryForm

# Create your views here.
def orders(request):

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = OrderForm()

    orders = Order.objects.all()
    entries = Entry.objects.all()
    context = {
        'orders': orders, 
        'entries': entries,
        'form': form,
    }
    return render(request, 'orders.html', context=context)

def order(request, id):

    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = EntryForm(initial={'orderID': id})

    entries = Entry.objects.filter(orderID=id)
    context = {
        'entries': entries,
        'form': form.as_div(),
    }
    return render(request, 'order.html', context=context)