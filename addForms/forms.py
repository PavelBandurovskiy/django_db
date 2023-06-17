from django import forms
from .models import Good, Client, Order

class Good_form(forms.ModelForm):
    class Meta:
        model = Good
        fields = ('goods_name', 'goods_type', 'rat', 'price',)

class Client_form(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('name', 'phone_number',)

class Order_form(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('goods_name', 'amount', 'name',)