"""Ecomm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from rest_framework.routers import DefaultRouter
from products.urls import ROUTER as product_router
from authentication.urls import ROUTER as authentication_router
from transaction.urls import ROUTER as transaction_router
from authentication.views import LoginView, LogoutView
class CommonRouter(DefaultRouter):
    """
    Router for Common Api-root for multiple apps and their urls
    full description of issue:
    https://github.com/tomchristie/django-rest-framework/pull/2001
    """
    def extend(self, router):
        """
        read the src:
        http://bit.ly/2jAzkbW
        """
        self.registry.extend(router.registry)

#https://www.python.org/dev/peps/pep-0008/#constants
ROUTER = CommonRouter()
ROUTER.extend(product_router)
ROUTER.extend(authentication_router)
ROUTER.extend(transaction_router)
SCHEMA_VIEW = get_schema_view(title='Ecomm API')

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='app/index.html'), name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(ROUTER.urls)),
    url(r'^auth/login/$', LoginView.as_view(), name='login'),
    url(r'^auth/logout/$', LogoutView.as_view(), name='logout'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^schema/$', SCHEMA_VIEW)
]
