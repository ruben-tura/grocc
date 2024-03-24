from django import forms
from .models import Order, Entry

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['title']

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        #fields = '__all__'
        exclude = ['total_price', 'discounted_price']
        labels = {
            'first_name': 'Nome',
            'last_name': 'Cognome',
            'club': 'Sala',
            'article': 'Articolo',
            'size': 'Taglia',
            'additional_notes': 'Note',
            'quantity': 'Quantità',
            'colour': 'Colore',
            'price': 'Prezzo',
        }