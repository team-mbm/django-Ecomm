"""
url regex for authentication/customer
"""
from django.conf.urls import url, include
from rest_framework import routers
from authentication.views import CustomerViewSet

ROUTER = routers.DefaultRouter()
"""
when you override get_queryset method from ModelViewSet you have to
define base_name otherwise there will be an
AssertionError: `base_name` argument not specified, and could
not automatically determine the name from the viewset,
as it does not have a `.queryset` attribute
"""
ROUTER.register(r'customer', CustomerViewSet, base_name='authentication-list')

urlpatterns = [
    url(r'^', include(ROUTER.urls)),
]