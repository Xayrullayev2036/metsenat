from rest_framework.routers import DefaultRouter
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView, TokenRefreshView
from sponsor.views import SponsorViewSet

router = DefaultRouter()
router.register("sponsor", SponsorViewSet, basename="sponsor")

urlpatterns = router.urls
