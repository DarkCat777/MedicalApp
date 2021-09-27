from rest_framework import routers

from apps.medical_check.views import MedicalCheckModelViewSet

router = routers.SimpleRouter()
router.register(r'', MedicalCheckModelViewSet)

urlpatterns = router.urls
