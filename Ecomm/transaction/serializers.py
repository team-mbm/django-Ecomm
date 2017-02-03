from transaction.models import Cart, CartItem
from rest_framework import serializers
class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ('cart', 'item', 'quantity')

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('items', 'customer', 'timestamp', 'total')
