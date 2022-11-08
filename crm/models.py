from django.db import models
from django.utils import timezone

#Define the model for the Customer table
class Customer(models.Model):
    cust_name = models.CharField(max_length=50)
    organization = models.CharField(max_length=20)
    role = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    bldgroom = models.CharField(max_length=50)
    account_number = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)

    def __str__ (self):
        return str(self.cust_name)



class Product(models.Model):

    customer_name = models.CharField(max_length=50)
    product_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    pickup_time = models.DateTimeField(
        default=timezone.localtime)
    charge = models.CharField(max_length=50)
    created_date = models.DateTimeField(
        default=timezone.localtime)

    def __str__(self):
        return str(self.customer_name)

class Service(models.Model):

    customer = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    email  = models.EmailField(max_length=100)
    description = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    setup_time = models.DateTimeField(
        default=timezone.localtime)
    cleanup_time = models.DateTimeField(
        default=timezone.localtime)
    service_charge = models.CharField(max_length=200)

    def __str__(self):
        return str(self.customer)
