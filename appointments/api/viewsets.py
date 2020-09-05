from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from appointments import models
from appointments.api import serializers


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = models.Appointment.objects.all()
    serializer_class = serializers.AppointmentSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = [
        "id",
        "date",
        "doctor__crm",
        "doctor__cpf",
        "doctor__occupation_area",
        "pacient__card_number",
        "pacient__cpf",
    ]

    def get_serializer_class(self):
        if self.action in ["retrieve", "list"]:
            return serializers.AppointmentDescriptionSerializer
        return serializers.AppointmentSerializer


class ExamHistoryViewSet(viewsets.ModelViewSet):
    queryset = models.ExamHistory.objects.all()
    serializer_class = serializers.ExamHistorySerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = [
        "id",
        "date",
        "lab",
        "doctor__crm",
        "doctor__cpf",
        "doctor__occupation_area",
        "pacient__card_number",
        "pacient__cpf",
    ]

    def get_serializer_class(self):
        if self.action in ["retrieve", "list"]:
            return serializers.ExamHistoryDescriptionSerializer
        return serializers.ExamHistorySerializer
