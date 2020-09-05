from rest_framework import viewsets

from accounts import models
from accounts.api import serializers


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = models.Doctor.objects.all()
    serializer_class = serializers.DoctorSerializer
    filter_fields = ('card_number')


class PacientViewSet(viewsets.ModelViewSet):
    queryset = models.Pacient.objects.all()
    serializer_class = serializers.PacientSerializer
    filter_fields = ('card_number')