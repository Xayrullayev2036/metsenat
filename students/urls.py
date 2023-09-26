from django.urls import path
from rest_framework.routers import DefaultRouter

from students.views import StudentViewSet, InstituteViewSet

router = DefaultRouter()
router.register("Students",StudentViewSet,basename="students")
router.register("Institute",InstituteViewSet,basename="students")

urlpatterns = router.urls


