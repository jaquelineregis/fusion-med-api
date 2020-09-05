from rest_framework import viewsets

from appointments import models
from appointments.api import serializers


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = models.Appointment.objects.all()
    serializer_class = serializers.AppointmentSerializer

    def get_serializer_class(self):
        if self.action in ['get', 'list']:
            return serializers.AppointmentDescriptionSerializer
        return serializers.AppointmentSerializer


class ExamHistoryViewSet(viewsets.ModelViewSet):
    queryset = models.ExamHistory.objects.all()
    serializer_class = serializers.ExamHistorySerializer

    def get_serializer_class(self):
        if self.action in ['get', 'list']:
            return serializers.AppointmentDescriptionSerializer
        return serializers.AppointmentSerializer
