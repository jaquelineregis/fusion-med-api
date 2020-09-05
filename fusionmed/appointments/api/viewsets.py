from rest_framework import viewsets

from appointments import models
from appointments.api import serializers


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = models.Appointment.objects.all()
    serializer_class = serializers.AppointmentSerializer


class ExamHistoryViewSet(viewsets.ModelViewSet):
    queryset = models.ExamHistory.objects.all()
    serializer_class = serializers.ExamHistorySerializer