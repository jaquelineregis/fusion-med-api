# from django.contrib.auth.models import User
from django.db import models


class Person(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    img_profile = models.ImageField()
    name = models.CharField(max_length=255)
    cpf = models.CharField(max_length=255, blank=True)
    email = models.EmailField()
    is_active = models.BooleanField(default=True)
    birth_date = models.DateField(max_length=255)
    phone = models.CharField(max_length=255, blank=True)
    cellphone = models.CharField(max_length=255, blank=True)
    emergency_phone = models.CharField(max_length=255, blank=True)
    emergency_contact_name = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    blood_type = models.CharField(max_length=255, blank=True)
    password = models.CharField(max_length=255, default="123456")

    def __str__(self):
        return self.name


class Doctor(Person):
    occupation_area = models.CharField(max_length=255)
    crm = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Pacient(Person):
    medical_record_number = models.CharField(max_length=255, blank=True)
    weight = models.CharField(max_length=255, blank=True)
    card_number = models.CharField(max_length=255)
    plan_type = models.CharField(max_length=255, blank=True)
    is_organ_donor = models.BooleanField(default=False)
    is_smoker = models.BooleanField(default=False)
    gender = models.CharField(max_length=255)
    limitations = models.TextField(blank=True)
    is_pregnant = models.BooleanField(default=False)
    allergies = models.CharField(max_length=255, blank=True)
    practice_exercises = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name
