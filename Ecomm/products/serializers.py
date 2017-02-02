"""
serializing our models so that it can be consumed as rest-api
"""

from products.models import Product
from rest_framework import serializers

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    """
    inherited from serializers.HyperlinkedModelSerializer
    to integrate with viewsets
    """
    class Meta:
        model = Product
        fields = ('id', 'url', 'title', 'price', 'company', 'image_url', 'stock',
                  'category')
