from django.urls import path
from . import views




urlpatterns=[
    path('customer_home',views.cust_home),
    path('customer_mycart',views.cust_cart),
    path('customer_cart',views.cust_carts),
    path('customer_products',views.cust_product),
    path('customer_profits',views.cust_profit),
     path('customer_changes',views.cust_change),
     path('customer_css',views.cust_css),
     path('customer_cssbox',views.cust_cssbox),
    path('customer_csspro',views.cust_csspro),
    path('customer_csspos',views.cust_csspos),
    path('customer_csssticky',views.cust_csssticky),
    path('customer_cssflexbox',views.cust_csssflexbox),
    path('customer_cssgrid',views.cust_csssgrid),
      
    
    
]