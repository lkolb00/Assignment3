from django import forms
from .models import Customer, Product, Service

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ( 'cust_name', 'organization', 'role', 'email', 'phone','bldgroom','account_number','address','city','state','zipcode')

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ( 'customer_name','product_name','description','quantity','pickup_time','charge','created_date')

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ('customer','category', 'email','description', 'location', 'setup_time', 'cleanup_time', 'service_charge')
