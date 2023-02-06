from django.shortcuts import render

# Create your views here.
def cust_home(request):
    return render(request,'customer/home.html')
    
def cust_cart(request):
    return render(request,'customer/mycart.html')  

def cust_carts(request):
     return render(request,'customer/cart.html')         

def cust_product(request):
     return render(request,'customer/product_details.html')   

def cust_profit(request):
     return render(request,'customer/profit.html')         

def cust_change(request):
     return render(request,'customer/change.html')              