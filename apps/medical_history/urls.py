from rest_framework import routers

from apps.medical_history.views import MedicalHistoryModelViewSet

router = routers.SimpleRouter()
router.register(r'', MedicalHistoryModelViewSet)

urlpatterns = router.urls
