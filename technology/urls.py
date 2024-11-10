from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RocketViewSet, SatelliteViewSet, MixedTechnologyView

router = DefaultRouter()
router.register(r'rockets', RocketViewSet)
router.register(r'satellites', SatelliteViewSet)

urlpatterns = [
    path('technology/', MixedTechnologyView.as_view(), name='technology'),
    path('', include(router.urls)),
]
