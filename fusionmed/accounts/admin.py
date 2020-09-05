from django.contrib import admin

from accounts import models

admin.site.register(models.Doctor)
admin.site.register(models.Pacient)
