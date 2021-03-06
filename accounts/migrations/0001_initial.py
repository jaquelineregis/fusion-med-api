# Generated by Django 3.0.8 on 2020-09-05 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Person",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("img_profile", models.ImageField(upload_to="")),
                ("name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
                ("is_active", models.BooleanField()),
                ("birth_date", models.DateField(max_length=255)),
                ("phone", models.CharField(max_length=255)),
                ("cellphone", models.CharField(max_length=255)),
                ("emergency_phone", models.CharField(max_length=255)),
                ("emergency_contact_name", models.CharField(max_length=255)),
                ("address", models.CharField(max_length=255)),
                ("blood_type", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Doctor",
            fields=[
                (
                    "person_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="accounts.Person",
                    ),
                ),
                ("occupation_area", models.CharField(max_length=255)),
                ("crm", models.CharField(max_length=255)),
            ],
            bases=("accounts.person",),
        ),
        migrations.CreateModel(
            name="Pacient",
            fields=[
                (
                    "person_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="accounts.Person",
                    ),
                ),
                ("medical_record_number", models.CharField(max_length=255)),
                ("card_number", models.CharField(max_length=255)),
                ("plan_type", models.CharField(max_length=255)),
                ("is_organ_donor", models.BooleanField()),
                ("is_smoker", models.BooleanField()),
                ("gender", models.CharField(max_length=255)),
                ("limitations", models.TextField()),
                ("is_pregnant", models.CharField(max_length=255)),
                ("allergies", models.CharField(max_length=255)),
                ("practice_exercises", models.CharField(max_length=255)),
            ],
            bases=("accounts.person",),
        ),
    ]
