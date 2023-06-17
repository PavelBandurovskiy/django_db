from django.contrib import admin
from .models import Good, Client, Order

@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
    list_display = ('goods_name', 'goods_type', 'rat', 'price')
    list_filter = ('goods_name', 'goods_type', 'rat', 'price')

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number')
    list_filter = ('name', 'phone_number')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('goods_name', 'amount', 'name')
    list_filter = ('goods_name', 'amount', 'name')

