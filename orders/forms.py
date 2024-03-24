from django import forms
from .models import Order, Entry

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['title']

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['orderID', 'first_name', 'last_name', 
        'club', 'article', 'size', 'additional_notes', 'quantity', 
        'colour', 'price', 'total_price', 'discounted_price']