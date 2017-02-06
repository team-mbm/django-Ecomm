from transaction.models import Cart, CartItem
from rest_framework import serializers
#debug this, senpai !!
class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = [
            "item",
            "quantity",
            "net_item_cost",
            ]
    def get_item(self, obj):
        return obj.item.id
    def get_net_item_cost(self, obj):
        return obj.quantity * obj.item.price
class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True) 
    class Meta:
        model = Cart
        fields = ('items', 'customer', 'timestamp', 'total_cost')

