from .models import Product, NewItem
from django import forms

class NewItemForm(forms.ModelForm):
    class Meta:
        model = NewItem
        fields = ["product_type","description","size","color","amount"]


class StockUpdateForm(forms.ModelForm):
    class Meta:
        model = NewItem
        fields = ["description","size","color","amount"]


class SaleForm(forms.ModelForm):
    class Meta:
        model = NewItem
        fields = ["amount"]


class NEWSTOCK(forms.ModelForm):
    class Meta:
        model = NewItem
        fields = ["amount"]
