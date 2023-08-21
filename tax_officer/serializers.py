from rest_framework import serializers
from . import models
from ..karer.serializers import Base64ImageField


class ViolationSerializer(serializers.ModelSerializer):
    car_photo = Base64ImageField(
        max_length=None, use_url=True,
    )

    class Meta:
        model = models.Violation
        fields = '__all__'
