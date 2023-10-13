from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter

from core.views import DashboardViewSet

router = DefaultRouter()
router.register("dashboards", DashboardViewSet, basename="dashboards")

urlpatterns = [
                  path('', include('sponsor.urls')),
                  path('', include('students.urls')),
                  path('auth/token/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
                  path('auth/token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
                  path('schema/', SpectacularAPIView.as_view(), name="schema"),
                  path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name="swagger-ui"),
                  path('schema/redoc/', SpectacularRedocView.as_view(url_name="schema"), name="redoc-view")
              ] + router.urls
