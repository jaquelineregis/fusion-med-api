from django.db import models

from accounts.models import Doctor, Pacient


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT)
    pacient = models.ForeignKey(Pacient, on_delete=models.PROTECT)
    date = models.DateTimeField()
    exams = models.TextField(blank=True)  # should be a ManyToMany
    # exams = models.ManyToManyField('Exam')

    def __str__(self):
        return str(self.date)


# class Exam(models.Model):
#     name = models.CharField(max_length=255)


class ExamHistory(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT, null=True)
    pacient = models.ForeignKey(Pacient, on_delete=models.PROTECT)
    lab = models.CharField(max_length=255, null=True)
    img = models.ImageField(null=True)
    file = models.FileField(null=True)
    date = models.DateField()

    class Meta:
        verbose_name_plural = "ExamHistories"

    def __str__(self):
        return str(self.id)
