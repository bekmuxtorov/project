from django.shortcuts import render
from rest_framework import generics

from . import models
from . import serializers


# Violation Create Api View
class ViolationCreateAPIView(generics.CreateAPIView):
    queryset = models.Violation.objects.all()
    serializer_class = serializers.ViolationSerializer


# Violation List API View
class ViolationListAPIView(generics.ListAPIView):
    queryset = models.Violation.objects.all()
    serializer_class = serializers.ViolationSerializer


# Violation Detail API View
class ViolationDetailAPIView(generics.RetrieveAPIView):
    queryset = models.Violation.objects.all()
    serializer_class = serializers.ViolationSerializer


# Violation Update API View
class ViolationUpdateAPIView(generics.UpdateAPIView):
    queryset = models.Violation.objects.all()
    serializer_class = serializers.ViolationSerializer


# Karer Delete API View
class ViolationDeleteAPIView(generics.DestroyAPIView):
    queryset = models.Violation.objects.all()
    serializer_class = serializers.ViolationSerializer
