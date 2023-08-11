from django.shortcuts import render
from rest_framework import generics

from . import models
from . import serializers


# Profile Create Api View
class ProfileCreateAPIView(generics.CreateAPIView):
    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer


# Profile List API View
class ProfileListAPIView(generics.ListAPIView):
    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer


# Profile Detail API View
class ProfileDetailAPIView(generics.RetrieveAPIView):
    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer


# Profile Update API View
class ProfileUpdateAPIView(generics.UpdateAPIView):
    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer


# Profile Delete API View
class ProfileDeleteAPIView(generics.DestroyAPIView):
    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer


# ************************************************************************************************ #


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
