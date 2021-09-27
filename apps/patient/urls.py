from rest_framework import routers

from apps.patient.views import PatientModelViewSet

router = routers.SimpleRouter()
router.register(r'', PatientModelViewSet)

urlpatterns = router.urls
