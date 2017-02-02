"""
views for Customer authentication
"""
from rest_framework import permissions, viewsets, status
from rest_framework.response import Response
from authentication.serializer import CustomerSerializer
from authentication.permissions import IsCustomerOwner
from authentication.models import Customer

class CustomerViewSet(viewsets.ModelViewSet):
    """
    customer viewset
    """

    lookup_field = 'username'
    serializer_class = CustomerSerializer
    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)
        if self.request.method == 'POST':
            return (permissions.AllowAny(),)
        return (IsCustomerOwner(), permissions.IsAuthenticated())

    def get_queryset(self):
        """
        only admin can see all users(i.e GET for admin only),
        only authenticated user can view `his` own account but not others,
        and any annonyms can create his account(i.e POST for all)
        """
        if self.request.user.is_staff:
            return Customer.objects.all()
        elif self.request.user.id:
            return Customer.objects.filter(id=self.request.user.id)
        else:
            return Customer.objects.none()
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            Customer.objects.create_user(**serializer.validated_data)
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

