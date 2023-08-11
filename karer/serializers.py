from rest_framework import serializers
from .models import Karer, Order


class KarerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Karer
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
