from django.shortcuts import render
from rest_framework import generics

from . import models
from . import serializers


# Order Create Api View
class OrderCreateAPIView(generics.CreateAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer


# Order List API View
class OrderListAPIView(generics.ListAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer


# Order Detail API View
class OrderDetailAPIView(generics.RetrieveAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer


# Order Update API View
class OrderUpdateAPIView(generics.UpdateAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer


# Order Delete API View
class OrderDeleteAPIView(generics.DestroyAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
