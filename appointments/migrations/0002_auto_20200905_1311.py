# Generated by Django 3.0.8 on 2020-09-05 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("appointments", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="examhistory",
            options={"verbose_name_plural": "ExamHistories"},
        ),
        migrations.AlterField(
            model_name="appointment",
            name="exams",
            field=models.TextField(blank=True),
        ),
    ]
