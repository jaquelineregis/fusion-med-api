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


class DoctorSingleDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Doctor
        fields = ['id', 'name', 'crm', 'occupation_area']


class PacientSingleDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pacient
        fields = ['id', 'name', 'card_number']