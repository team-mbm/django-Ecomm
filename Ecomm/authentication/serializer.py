"""
serializing customer model
"""
from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers
from authentication.models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    """
    seraializing Customer Model
    """
    password = serializers.CharField(write_only=True, required=True,
                                     style={'input_type':'password'})
    confirm_password = serializers.CharField(write_only=True, required=True,
                                             style={'input_type':'password'})
    class Meta:
        model = Customer
        fields = ('id', 'email', 'username', 'first_name', 'last_name',
                  'address', 'password', 'confirm_password')
    def validate(self, attrs):
        if attrs['password'] != attrs.pop('confirm_password'):
            raise serializers.ValidationError("Passwords do not match")
        return attrs
    def create(self, validated_data):
        return Customer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.save()
        password = validated_data.get('password', None)
        confirm_password = validated_data.get('confirm_password', None)
        if password and confirm_password and password == confirm_password:
            instance.set_password(password)
            instance.save()
        update_session_auth_hash(self.context.get('request'), instance)
        return instance
