from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FlightScheduleViewSet

router = DefaultRouter()
router.register(r'', FlightScheduleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
