from django.urls import path, include
from rest_framework import routers

from appointments.api import viewsets

router = routers.DefaultRouter()
router.register(r'appointments', viewsets.AppointmentViewSet, basename='appointments')
router.register(r'exam_histories', viewsets.ExamHistoryViewSet, basename='exam_histories')
urlpatterns = router.urls