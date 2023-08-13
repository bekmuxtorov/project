from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from . import models
from . import serializers

from .sent_sms_infobip import sent_sms_to_phone_number


@swagger_auto_schema(
    operation_description="Send code",
    methods=['post'],
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['phone_number', 'password'],
        properties={
            'phone_number': openapi.Schema(type=openapi.TYPE_STRING, description='Phone number'),
            'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password'),
        }
    ),
    responses={
        200: openapi.Response(
            description="Send code",
            examples={
                'application/json':  {
                        'status': 200,
                        'message': 'Code sent'
                }
            }
        ),
        400: openapi.Response(
            description="Bad request",
            examples={
                'application/json': {
                        'status': 400,
                        'message': ""
                }
            }
        )
    }
)
@api_view(['POST'])
@permission_classes([AllowAny,])
def sent_verification_code(request):
    data = request.data
    if data.get('phone_number') is None:
        return Response(
            {
                'status': 400,
                'message': 'Phone number is required'
            }
        )

    if data.get('password') is None:
        return Response(
            {
                'status': 400,
                'message': 'Password is required'
            }
        )

    phone_number = data.get('phone_number')
    if len(phone_number) != 12:
        return Response(
            {
                'status': 400,
                'message': "The phone number must be entered as follows: 901234567"
            }
        )

    if not models.Account.objects.filter(phone_number=phone_number).exists():
        user = models.Account.objects.create(
            phone_number=phone_number,
            sms_code=sent_sms_to_phone_number(
                phone_number=phone_number
            )
        )
        user.set_password = data.get('set_password')
        user.save()

    else:
        user = models.Account.objects.get(phone_number=phone_number)
        user.sms_code = sent_sms_to_phone_number(
            phone_number=phone_number
        )
        user.set_password = data.get('set_password')
        user.save()

    return Response(
        {
            'status': 200,
            'message': 'Code sent'
        }
    )


@swagger_auto_schema(
    operation_description="Verify code",
    methods=['post'],
    request_body=openapi.Schema(
        required=['phone_number', 'sms_code'],
        type=openapi.TYPE_OBJECT,
        properties={
            'phone_number': openapi.Schema(type=openapi.TYPE_STRING, description='Phone number'),
            'sms_code': openapi.Schema(type=openapi.TYPE_STRING, description='Password'),
        }
    ),
    responses={
        200: openapi.Response(
            description="Verify code",
            examples={
                'application/json': {
                        'status': 200,
                        'message': 'Verify code'
                }
            }
        ),
        400: openapi.Response(
            description="Bad request",
            examples={
                'application/json': {
                        'status': 400,
                        'message': 'Invalid code'
                }
            }
        )
    }
)
@api_view(['POST'])
@permission_classes([AllowAny,])
def verify_code(request):
    data = request.data
    if data.get('phone_number') is None:
        return Response(
            {
                'status': 400,
                'message': 'Phone number is required'
            }
        )

    if data.get('sms_code') is None:
        return Response(
            {
                'status': 400,
                'message': 'sms code is required'
            }
        )
    phone_number = data.get('phone_number')
    if len(phone_number) != 12:
        return Response(
            {
                'status': 400,
                'message': "The phone number must be entered as follows: 998901234567"
            }
        )

    if not models.Account.objects.filter(phone_number=phone_number).exists():
        return Response(
            {
                'status': 400,
                'message': 'Invalid phone number'
            }
        )
    user = models.Account.objects.filter(phone_number=phone_number).first()

    if user.sms_code == data.get('sms_code'):
        user.is_phone_verified = True
        user.save()
        return Response({
            'status': 200,
            'message': 'Verify code'
        })

    return Response({
        'status': 400,
        'message': 'Invalid code'
    })


class KarerRegisterAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = serializers.KarerRegisterSerializer

    @swagger_auto_schema(
        operation_description="Registration karer user",
        request_body=openapi.Schema(
            required=['phone_number', 'karer_name', 'password', 'password2'],
            type=openapi.TYPE_OBJECT,
            properties={
                'phone_number': openapi.Schema(type=openapi.TYPE_STRING, description="Phone number"),
                'karer_name': openapi.Schema(type=openapi.TYPE_STRING, description="Karer name"),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password'),
                'password2': openapi.Schema(type=openapi.TYPE_STRING, description='Password'),
            }
        ),
        responses={
            200: openapi.Response(
                description="Karer user registration",
                examples={
                    'application/json': {
                        "refresh": "8l6YUaZzRQMq2LSowJXWQUNxWbYzDwXPc",
                        "access": "nlMMPgyNm9GQprEm0aedNP4dWOCL5HUuNeU",
                        "user": {
                            "phone_number": "998901234567",
                            "karer_name": "Palonchi"
                        }
                    }
                }
            ),
            400: openapi.Response(
                description="Bad request",
                examples={
                    'application/json': {
                            'error': 'Invalid credentials'
                    }
                }
            )
        }
    )
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            refresh = RefreshToken.for_user(user)
            response_data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': serializer.data,
            }

            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaxOfficerRegisterAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = serializers.TaxOfficerRegisterSerializer

    @swagger_auto_schema(
        operation_description="Registration tax officer user",
        request_body=openapi.Schema(
            required=[
                'phone_number', 'full_name', 'passport_or_id', 'password_or_id_number',
                'position',  'working_region', 'password', 'password2'
            ],
            type=openapi.TYPE_OBJECT,
            properties={
                'phone_number': openapi.Schema(type=openapi.TYPE_STRING, description="Phone number"),
                'full_name': openapi.Schema(type=openapi.TYPE_STRING, description="Full name"),
                'passport_or_id': openapi.Schema(type=openapi.TYPE_STRING, enum=['passport', 'document_id'], description='passport_or_id'),
                'password_or_id_number': openapi.Schema(type=openapi.TYPE_STRING, description="Password or id number"),
                'position': openapi.Schema(type=openapi.TYPE_STRING, description="Position"),
                'working_region': openapi.Schema(type=openapi.TYPE_NUMBER, enum=list(models.Region.objects.values_list('name', flat=True)), description="Working Region"),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password'),
                'password2': openapi.Schema(type=openapi.TYPE_STRING, description='Password'),
            }
        ),
        responses={
            200: openapi.Response(
                description="Karer user registration",
                examples={
                    'application/json': {
                        "refresh": "EK9K9XLSKZbi2v7aZnAPAYrQDUEcFNPHWz2Os",
                        "access": "Hy5XXsokKRXIi0sfZnflKaYCZ_goE96-iqg",
                        "user": {
                            "phone_number": "998771234567",
                            "full_name": "Topvoldi",
                            "passport_or_id": "passport",
                            "password_or_id_number": "1234567",
                            "position": "Ishchi",
                            "working_region": 1
                        }
                    }
                }
            ),
            400: openapi.Response(
                description="Bad request",
                examples={
                    'application/json': {
                            'error': 'Invalid credentials'
                    }
                }
            )
        }
    )
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            response_data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': serializer.data,
            }

            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Region Create Api View
class RegionCreateAPIView(generics.CreateAPIView):
    queryset = models.Region.objects.all()
    serializer_class = serializers.RegionSerializer


# Region List API View
class RegionListAPIView(generics.ListAPIView):
    queryset = models.Region.objects.all()
    serializer_class = serializers.RegionSerializer


# Region Detail API View
class RegionDetailAPIView(generics.RetrieveAPIView):
    queryset = models.Region.objects.all()
    serializer_class = serializers.RegionSerializer


# Region Update API View
class RegionUpdateAPIView(generics.UpdateAPIView):
    queryset = models.Region.objects.all()
    serializer_class = serializers.RegionSerializer


# Region Delete API View
class RegionDeleteAPIView(generics.DestroyAPIView):
    queryset = models.Region.objects.all()
    serializer_class = serializers.RegionSerializer
