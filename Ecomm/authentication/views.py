"""
views for Customer authentication
"""
import json
from django.contrib.auth import authenticate, login, logout
from rest_framework import permissions, viewsets, views, status
from rest_framework.response import Response
from authentication.serializer import CustomerSerializer
from authentication.permissions import IsCustomerOwner
from authentication.models import Customer

class LoginView(views.APIView):
    """
    view for customer login
    """
    def post(self, request, format=None):
        data = json.loads(request.body)
        email = data.get('email', None)
        password = data.get('password', None)
        customer = authenticate(email=email, password=password)
        if customer is not None:
            if customer.is_active:
                login(request, customer)
                serialized = CustomerSerializer(customer)
                return Response(serialized.data)
            else:
                return Response({
                    'status': 'Unauthorized',
                    'message': 'This account has been disabled.'
                }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({
                'status':'Unauthorized',
                'message':'Username/password are invalid'
            }, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def post(self, request, format=None):
        print(request)
        logout(request)
        return Response({}, status=status.HTTP_204_NO_CONTENT)

class CustomerViewSet(viewsets.ModelViewSet):
    """
    customer viewset i.e customer list and info.
    **only admin can view all customer's info(but not password since they are encrypted)
    and customer himself can only view his own info
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

