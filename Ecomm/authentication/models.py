"""
db-model for customer
"""
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class CustomerManager(BaseUserManager):
    """
    managing customer model for api
    """
    def create_user(self, email, password=None, **kwargs):
        """
        POST on customer model
        """
        if not email:
            raise ValueError("Customer must have valid email address")
        if not kwargs.get('username'):
            raise ValueError("Customer must have a valid & unique username")
        if not kwargs.get('address'):
            raise ValueError("Customer must have an address")
        customer = self.model(
            email=self.normalize_email(email), username=kwargs.get('username'),
            address=kwargs.get('address')
            )
        customer.set_password(password)
        customer.save()
        return customer

    def create_superuser(self, email, password, **kwargs):
        """
        for admin
        """
        customer = self.create_user(email, password, **kwargs)
        customer.is_admin = True
        customer.save()
        return customer

class Customer(AbstractBaseUser):
    """
    Customer => {`email`,`username`,`first_name`,`last_name`,`password`,`address`}
    """
    address = models.TextField(blank=False)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    objects = CustomerManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'address']
    is_admin = models.BooleanField(default=False)

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    def __unicode__(self):
        return self.email

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])

    def get_short_name(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
