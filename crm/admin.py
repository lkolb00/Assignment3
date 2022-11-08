from django.contrib import admin
from .models import Customer, Product, Service

#Define the admin options for the Customer table
class CustomerList(admin.ModelAdmin):
    list_display = ('cust_name', 'organization')
    list_filter = ('cust_name', 'organization')
    search_fields = ('cust_name', 'organization')
    ordering = ['cust_name']

#Define the admin options for the Service table
class ProductList(admin.ModelAdmin):
    list_display = ( 'customer_name', 'product_name')
    list_filter = ( 'customer_name', 'product_name')
    search_fields = ( 'customer_name', 'product_name')
    ordering = ['customer_name']

#Define the admin options for the Product table
class ServiceList(admin.ModelAdmin):
    list_display = ( 'customer', 'category')
    list_filter = ( 'customer', 'category')
    search_fields = ( 'customer', 'category')
    ordering = ['customer']



admin.site.register(Customer, CustomerList)
admin.site.register(Product, ProductList)
admin.site.register(Service, ServiceList)
