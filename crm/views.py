from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import *
from.forms import *

def home(request):
    orders=Order.objects.all()
    customers=Customer.objects.all()

    total_customers = customers.count()

    total_orders=orders.count()
    served=orders.filter(status='Served').count()
    pending = orders.filter(status='Pending').count()
    unpaid = orders.filter(status='Unpaid').count()
    paid = orders.filter(status='Paid').count()

    context={'orders':orders,'customers':customers,
    'total_orders':total_orders,'served':served,'pending':pending,'unpaid':unpaid,'paid':paid}
     
    return render(request,'crm/dashboard.html',context)

def products(request):
    products=Product.objects.all()
    return render(request,'crm/products.html',{'Products':products})

def customer(request, pk_test):
    customer=Customer.objects.get(id=pk_test)
    customer=Customer.objects.all() 

    return render(request,'crm/customer.html',{'Customer':customer})


def createOrder(request):

    form = Orderform()
    if request.method == 'POST':
        form=Orderform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')


    context={'form':form}

    return render(request,'crm/order_form.html',context)

def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = Orderform(instance=order)
     
    if request.method == 'POST':
        form=Orderform(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'crm/order_form.html',context)

def deleteOrder(request,pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')
    context={'item':order}
    return render(request, 'crm/delete.html',context)