from django.urls import path
from . import views




urlpatterns=[
    path('customer_home',views.cust_home),
    path('customer_mycart',views.cust_cart),
    path('customer_cart',views.cust_carts),
    path('customer_products',views.cust_product),
    path('customer_profits',views.cust_profit),
     path('customer_changes',views.cust_change),
    
]