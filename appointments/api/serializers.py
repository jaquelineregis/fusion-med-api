from rest_framework import serializers

from accounts.api.serializers import (
    DoctorSingleDescriptionSerializer,
    PacientSingleDescriptionSerializer,
)
from appointments import models


class AppointmentDescriptionSerializer(serializers.ModelSerializer):
    doctor = DoctorSingleDescriptionSerializer()
    pacient = PacientSingleDescriptionSerializer()
    date_f = serializers.DateTimeField(read_only=True)

    class Meta:
        model = models.Appointment
        fields = "__all__"


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Appointment
        fields = "__all__"


class ExamHistoryDescriptionSerializer(serializers.ModelSerializer):
    doctor = DoctorSingleDescriptionSerializer()
    pacient = PacientSingleDescriptionSerializer()
    date_f = serializers.DateField(read_only=True)

    class Meta:
        model = models.ExamHistory
        fields = "__all__"


class ExamHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ExamHistory
        fields = "__all__"
