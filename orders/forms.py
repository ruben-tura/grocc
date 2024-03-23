from django import forms
from .models import Order, Entry

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['title']

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['orderID', 'article', 'quantity', 'colour', 'price']