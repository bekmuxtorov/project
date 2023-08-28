from rest_framework import serializers

from . import models
from karer import serializers as general_serializers
from account.serializers import TaxOfficerSerializer


class ViolationSerializer(serializers.ModelSerializer):
    tax_officer = TaxOfficerSerializer(read_only=True)
    created_at = serializers.DateTimeField(format="%d.%m.%Y %H:%M")
    cargo_date = serializers.DateTimeField(format="%d.%m.%Y %H:%M")

    class Meta:
        model = models.Violation
        fields = '__all__'


class ViolationCreateSerializer(serializers.ModelSerializer):
    car_photo = general_serializers.Base64ImageField(
        max_length=None, use_url=True,
    )

    class Meta:
        model = models.Violation
        fields = '__all__'
