from django.shortcuts import render, redirect, get_object_or_404
from .forms import Client_form, Order_form, Good_form
from .models import Good, Client, Order

def client(request):
    data = Client.objects.all()
    if request.method == "POST":
        form = Client_form(request.POST)
        if form.is_valid():
            cl = form.save(commit=False)
            cl.save()
            return redirect("client")
    else:
        form = Client_form()
    return render(request, 'addForms/client.html', {'form': form, 'data': data})

def good(request):
    data = Good.objects.all()
    if request.method == "POST":
        form = Good_form(request.POST)
        if form.is_valid():
            gd = form.save(commit=False)
            gd.save()
            return redirect("good")
    else:
        form = Good_form()
    return render(request, 'addForms/good.html', {'form': form, 'data':data})

def order(request):
    data = Order.objects.all()
    if request.method == "POST":
        form = Order_form(request.POST)
        if form.is_valid():
            ord = form.save(commit=False)
            ord.save()
            return redirect("order")
    else:
        form = Order_form()
    return render(request, 'addForms/order.html', {'form': form, 'data':data})

def delete_good(request, id):
    Good.objects.filter(goods_name = id).delete()
    return redirect('good')

def delete_client(request, id):
    Client.objects.filter(id=id).delete()
    return redirect('client')

def delete_order(request, id):
    Order.objects.filter(id=id).delete()
    return redirect('order')