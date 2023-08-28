from rest_framework import serializers

from . import models


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Region
        fields = '__all__'


class KarerRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = models.Account
        fields = [
            'phone_number', 'karer_name', 'password', 'password2'
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'password2': {'write_only': True},
        }

    def create(self, validated_data):
        phone_number = validated_data.get('phone_number')
        karer_name = validated_data.get('karer_name')
        password = validated_data.get('password')
        password2 = validated_data.get('password2')

        if password == password2:
            user = models.Account(
                type='karer',
                karer_name=karer_name,
                phone_number=phone_number
            )
            user.set_password(password)
            user.save()
            return user
        else:
            raise serializers.ValidationError({
                'error': 'Both passwords do not match'
            })


class TaxOfficerRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = models.Account
        fields = [
            'phone_number', 'full_name', 'passport_or_id', 'password_or_id_number',
            'position',  'working_region', 'password', 'password2'
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'password2': {'write_only': True},
        }

    def create(self, validated_data):
        phone_number = validated_data.get('phone_number')
        full_name = validated_data.get('full_name')
        passport_or_id = validated_data.get('passport_or_id')
        password_or_id_number = validated_data.get('password_or_id_number')
        position = validated_data.get('position')
        working_region = validated_data.get('working_region')
        password = validated_data.get('password')
        password2 = validated_data.get('password2')

        if password == password2:
            user = models.Account(
                type='tax_officer',
                phone_number=phone_number,
                full_name=full_name,
                passport_or_id=passport_or_id,
                password_or_id_number=password_or_id_number,
                position=position,
                working_region=working_region
            )
            user.set_password(password)
            user.save()
            return user
        else:
            raise serializers.ValidationError({
                'error': 'Both passwords do not match'
            })


class KarerSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    phone_number = serializers.CharField(max_length=20)
    karer_name = serializers.CharField(max_length=100)


class TaxOfficerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Account
        exclude = ['type', 'karer_name', 'password',
                   'last_login', 'is_superuser', 'groups', 'user_permissions']
