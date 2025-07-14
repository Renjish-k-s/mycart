from django.db import models
from customers.models import Customer
from products.models import Product

# model to store cart details


class Orders(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((LIVE, 'Live'), (DELETE, 'Delete'))

    CART_STAGE=0
    ORDER_CONFIRMED=1
    ORDER_PROCESSED=2
    ORDER_DELIVERED=3
    ORDER_REJECTED=4    

    STATUS_CHOICES = (
        (ORDER_PROCESSED, 'Order Processed'),
        (ORDER_DELIVERED, 'Order Delivered'),   
        (ORDER_REJECTED, 'Order Rejected'),
    )
    order_status = models.IntegerField(choices=STATUS_CHOICES, default=CART_STAGE)
    owner = models.ForeignKey(Customer, on_delete=models.SET_NULL, related_name='carts',null=True)
    delete_status = models.IntegerField(choices=DELETE_CHOICES, default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OrderedItems(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL, related_name='cart_items', null=True)
    quantity = models.IntegerField(default=1)
    owner = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name='ordered_items')


        




