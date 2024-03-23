from django.shortcuts import render
from .models import Order, Entry
from .forms import OrderForm

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