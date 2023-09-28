from django.urls import path
from rest_framework.routers import DefaultRouter

from students.views import StudentViewSet, InstituteViewSet

router = DefaultRouter()
router.register("students",StudentViewSet,basename="students")
router.register("institute",InstituteViewSet,basename="students")

urlpatterns = router.urls


