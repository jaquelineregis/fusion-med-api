from rest_framework import routers

from accounts.api import viewsets

router = routers.DefaultRouter()
router.register(r"doctors", viewsets.DoctorViewSet, basename="doctors")
router.register(r"pacients", viewsets.PacientViewSet, basename="pacients")
urlpatterns = router.urls
