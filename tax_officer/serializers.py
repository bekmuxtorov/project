from rest_framework import serializers
from . import models


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        fields = '__all__'


class ViolationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Violation
        fields = '__all__'
