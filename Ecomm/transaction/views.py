from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from transaction.serializers import CartSerializer, CartItemSerializer
from transaction.models import Cart, CartItem

# Create your views here.
class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]
class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]
