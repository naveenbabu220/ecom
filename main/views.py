from django.shortcuts import render,get_object_or_404,redirect
from.models import Types,Cat,OrderItem,Payment,Order
from django .views.generic import View,ListView,DetailView
from .form import Address
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
def home(req):
    cat = Cat.objects.all()
    types = Types.objects.all()
    return render(req,'main/home.html',{'cat': cat,'types':types})

def cat(req):
    cat = Cat.objects.all()
    return render(req,'main/cat.html',{'cat': cat})

    
def types(req,idd):
    cat = Cat.objects.get(cat = idd)
    return render(req,'main/type.html',{'cat':cat})

@login_required
def add_to_cart(req,slug):
    types = get_object_or_404(Types,slug = slug)
    order_iteam , created = OrderItem.objects.get_or_create(types = types,user = req.user,orderd=False)
    order_qs = Order.objects.filter(user = req.user,orderd = False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(types__slug = types.slug).exists():
            order_iteam.quanty += 1
            order_iteam.save()
            return redirect('home')
        else:
            order.items.add(order_iteam)
            return redirect('home')
    else:
        order = Order.objects.create(user = req.user,orderd = False)
        order.items.add(order_iteam)
        return redirect('home')

    return render(req,'main/orderitem.html',{})

@login_required
def remove_from_cart(req,slug):
    types = get_object_or_404(Types,slug = slug)
    order_qs = Order.objects.filter(user = req.user,orderd = False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(types__slug = types.slug).exists():
            order_iteam = OrderItem.objects.filter(types = types,user = req.user,orderd=False)[0]
            order_iteam.quanty = 1
            order_iteam.save()
            order.items.remove(order_iteam)
            return redirect('home')
        else:
            return redirect('home')
    else:
        return redirect('home')

def summary(req):
    order = Order.objects.get(user = req.user,orderd= False)
    return render(req,'main/summary.html',{'order':order})

def payment(req):
    order = Order.objects.get(user=req.user,orderd=False)
    if order.address is not None and order.country is not None:
        return render(req,'main/payment.html',{'order':order})
    else:
        if req.method == 'POST':
            form = Address(req.POST)
            if form.is_valid():    
                order.address = form.cleaned_data.get('address')
                order.country = form.cleaned_data.get('country')
                order.save()
        else:
            form = Address()            
        return render(req,'main/address.html',{'form':form})
def address(req,id):
    order = get_object_or_404(Order,id = id)
    form = Address(req.POST,instance = order)
    if req.method == 'POST':
        
        if form.is_valid():    
            order.address = form.cleaned_data.get('address')
            order.country = form.cleaned_data.get('country')
            order.save()
        return render(req,'main/addres.html',{'form':form})
    else:
        form = Address()            
    #return render(req,'main/addres.html',{'form':form})






