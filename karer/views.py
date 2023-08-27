from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from . import models
from . import serializers


@api_view(['GET',])
@permission_classes([IsAuthenticated])
def orders_by_karer_id(request, karer_id):
    orders = models.Order.objects.filter(karer_id=karer_id)
    serializer = serializers.OrderSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(['GET',])
@permission_classes([IsAuthenticated])
def orders_by_unique_number(request, unique_number):
    try:
        order = models.Order.objects.filter(unique_number=unique_number)
        serializer = serializers.OrderSerializer(order, many=True)
        return Response(serializer.data)
    except:
        return Response({'error': 'No object matching this unique_number exists'}, status=400)


# Order Create Api View
class OrderCreateAPIView(generics.CreateAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer


# Order List API View
class OrderListAPIView(generics.ListAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderListSerializer


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
