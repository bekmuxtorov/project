from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from . import models
from . import serializers


@api_view(['GET',])
@permission_classes([IsAuthenticated])
def violation_by_unique_number(request, unique_number):
    try:
        violation = models.Violation.objects.filter(unique_number=unique_number)
        serializer = serializers.ViolationSerializer(violation, many=True)
        return Response(serializer.data)
    except:
        return Response({'error': 'No object matching this unique_number exists'}, status=400)


# Violation Create Api View
class ViolationCreateAPIView(generics.CreateAPIView):
    queryset = models.Violation.objects.all()
    serializer_class = serializers.ViolationCreateSerializer


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
    serializer_class = serializers.ViolationCreateSerializer


# Karer Delete API View
class ViolationDeleteAPIView(generics.DestroyAPIView):
    queryset = models.Violation.objects.all()
    serializer_class = serializers.ViolationSerializer
