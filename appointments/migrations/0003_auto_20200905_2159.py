# Generated by Django 3.0.8 on 2020-09-05 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("appointments", "0002_auto_20200905_1311"),
    ]

    operations = [
        migrations.AlterField(
            model_name="examhistory",
            name="file",
            field=models.FileField(null=True, upload_to="appointments/exam/file"),
        ),
        migrations.AlterField(
            model_name="examhistory",
            name="img",
            field=models.ImageField(null=True, upload_to="appointments/exam/img"),
        ),
    ]