"""
object models used for product app
"""
from __future__ import unicode_literals
from django.db import models
class Product(models.Model):
    """
    product model with attributes such title,price,
    category,stock,image
    """
    title = models.CharField(max_length=100, blank=False)
    price = models.IntegerField(blank=False)
    category = models.CharField(max_length=100, blank=False)
    stock = models.IntegerField(blank=False)
    image_url = models.URLField(blank=False)
    company = models.CharField(max_length=100, blank=False)
    def __unicode__(self):
        return self.title + " | " + self.company

