"""
url regex
"""
from django.conf.urls import url, include
from products import views
from rest_framework.routers import DefaultRouter
#all-caps becoz of fuckin pylint warnings, also module-level constants should be capital
ROUTER = DefaultRouter()
ROUTER.register(r'product', views.ProductViewSet)

urlpatterns = [
    url(r'^', include(ROUTER.urls)),
    url(r'^$', views.IndexView.as_view(), name='index'),

]
