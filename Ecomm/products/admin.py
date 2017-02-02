"""
registering models for admin-panel
"""
from django.contrib import admin
from products.models import Product
admin.site.register(Product)
