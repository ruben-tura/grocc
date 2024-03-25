from django import forms
from django.forms import TextInput, Textarea, NumberInput, Select
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
            'orderID': '',
        }
        widgets = {
            'first_name': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Nome'
                }),
            'last_name': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Cognome'
                }),
            'club': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Sala'
                }),
            'article': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Articolo'
                }),
            'size': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Taglia'
                }),
            'additional_notes': Textarea(attrs={
                'class': "form-control",
                'placeholder': 'Note'
                }),
            'quantity': NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'Quantità'
                }),
            'colour': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Colore'
                }),
            'price': NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'Prezzo'
                }),
            'orderID': Select(attrs={
                'class': "form-control",
                'style': 'display: none;',
                'placeholder': 'Order ID'
                }),
        }