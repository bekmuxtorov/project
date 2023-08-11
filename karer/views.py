from django.shortcuts import render
from rest_framework import generics

from . import models
from . import serializers


# Karer Create Api View
class KarerCreateAPIView(generics.CreateAPIView):
    queryset = models.Karer.objects.all()
    serializer_class = serializers.KarerSerializer


# Karer List API View
class KarerListAPIView(generics.ListAPIView):
    queryset = models.Karer.objects.all()
    serializer_class = serializers.KarerSerializer


# Karer Detail API View
class KarerDetailAPIView(generics.RetrieveAPIView):
    queryset = models.Karer.objects.all()
    serializer_class = serializers.KarerSerializer


# Karer Update API View
class KarerUpdateAPIView(generics.UpdateAPIView):
    queryset = models.Karer.objects.all()
    serializer_class = serializers.KarerSerializer


# Karer Delete API View
class KarerDeleteAPIView(generics.DestroyAPIView):
    queryset = models.Karer.objects.all()
    serializer_class = serializers.KarerSerializer


# ************************************************************************************************ #


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
