from django.contrib import admin

from appointments import models

admin.site.register(models.Appointment)
admin.site.register(models.ExamHistory)

