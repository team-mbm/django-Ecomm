"""
the view part of mvc model
"""
from rest_framework import viewsets
from products.models import Product
from products.serializers import ProductSerializer
from products.permissions import IsAdminOrReadOnly
#http://django-rest-framework.readthedocs.io/en/latest/api-guide/viewsets/
class ProductViewSet(viewsets.ModelViewSet):
    """
    GET requests for product/ & product/<pk>
    all CRUD for admin/superuser
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]
