from django.conf.urls import url, include
from transaction import views
from rest_framework.routers import DefaultRouter
#all-caps becoz of fuckin pylint warnings, also module-level constants should be capital
ROUTER = DefaultRouter()
ROUTER.register(r'cartitem', views.CartItemViewSet)
ROUTER.register(r'cart', views.CartViewSet)
urlpatterns = [
    url(r'^', include(ROUTER.urls)),
]