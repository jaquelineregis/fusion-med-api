from rest_framework import serializers

from accounts import models


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Doctor
        fields = '__all__'


class PacientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pacient
        fields = '__all__'