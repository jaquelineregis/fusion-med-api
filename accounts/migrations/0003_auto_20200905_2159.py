# Generated by Django 3.0.8 on 2020-09-05 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_auto_20200905_1311"),
    ]

    operations = [
        migrations.AlterField(
            model_name="person",
            name="img_profile",
            field=models.ImageField(upload_to="accounts/profile"),
        ),
    ]