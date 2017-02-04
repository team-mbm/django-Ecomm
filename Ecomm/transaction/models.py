from __future__ import unicode_literals, print_function
from decimal import Decimal
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save, post_delete
from authentication.models import Customer
from products.models import Product

"""
This shit is confusing
http://bit.ly/2l634cR
http://bit.ly/2l63f81
"""
class CartItem(models.Model):
    cart = models.ForeignKey("Cart")
    item = models.ForeignKey(Product)
    quantity = models.PositiveIntegerField(default=0)
    net_item_cost = models.PositiveIntegerField(default=0, blank=True, null=True)
    def __unicode__(self):
        print(self.item)
        return self.item.title + " | " + self.item.company


def calc_item_cost(sender, instance, *args, **kwargs):
    """
    update cost field for a perticular item in cart.
    do a simple test in http://localhost:8000/admin/cart
    """
    if instance.quantity >= 1:
        instance.net_item_cost = instance.quantity*instance.item.get_price()
    else:
        instance.net_item_cost = 0

pre_save.connect(calc_item_cost, sender=CartItem)

def calc_total_cost_update(sender, instance, *args, **kwargs):
    """
    update total_cost field whenever we add/delete an item
    thats why both signals(i.e save & delete) are called
    """
    instance.cart.update_total_cost()

post_save.connect(calc_total_cost_update, sender=CartItem)
post_delete.connect(calc_total_cost_update, sender=CartItem)
class Cart(models.Model):
    """
    http://bit.ly/2l63HTL
    """
    items = models.ManyToManyField(Product, through=CartItem)
    customer = models.ForeignKey(settings.AUTH_USER_MODEL)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    total_cost = models.DecimalField(max_digits=30, decimal_places=2, blank=True, null=True)
    def __unicode__(self):
        return self.customer.username + "  |  " + str(self.total_cost)
    def update_total_cost(self):
        """
        explaination of ManyToMany field
        http://bit.ly/2kBwFOo
        """
        items = self.cartitem_set.all()
        print("updaing total_cost field in Cart..........")
        self.total_cost = Decimal(sum([item.net_item_cost for item in items]))
        print(self.total_cost)
        self.save()

