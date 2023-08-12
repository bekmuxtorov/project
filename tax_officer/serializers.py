from rest_framework import serializers
from . import models


class ViolationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Violation
        fields = '__all__'
