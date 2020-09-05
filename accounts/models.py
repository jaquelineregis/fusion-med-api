# from django.contrib.auth.models import User
from django.db import models


class Person(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    img_profile = models.ImageField(blank=False, null=False)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    is_active = models.BooleanField()
    birth_date = models.DateField(max_length=255)
    phone = models.CharField(max_length=255)
    cellphone = models.CharField(max_length=255)
    emergency_phone = models.CharField(max_length=255)
    emergency_contact_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    blood_type = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Doctor(Person):
    occupation_area = models.CharField(max_length=255)
    crm = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Pacient(Person):
    medical_record_number = models.CharField(max_length=255)
    card_number = models.CharField(max_length=255)
    plan_type = models.CharField(max_length=255)
    is_organ_donor = models.BooleanField()
    is_smoker = models.BooleanField()
    gender = models.CharField(max_length=255)
    limitations = models.TextField()
    is_pregnant = models.CharField(max_length=255)
    allergies = models.CharField(max_length=255)
    practice_exercises = models.CharField(max_length=255)

    def __str__(self):
        return self.name
