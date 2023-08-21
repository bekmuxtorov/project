from rest_framework import serializers
from . import models
from karer import serializers as general_serializers


class ViolationSerializer(serializers.ModelSerializer):
    car_photo = general_serializers.Base64ImageField(
        max_length=None, use_url=True,
    )

    class Meta:
        model = models.Violation
        fields = '__all__'
