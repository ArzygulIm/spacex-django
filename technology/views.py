from rest_framework import viewsets
from .models import Rocket, Satellite
from .serializers import RocketSerializer, SatelliteSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class RocketViewSet(viewsets.ModelViewSet):
    queryset = Rocket.objects.all()
    serializer_class = RocketSerializer

class SatelliteViewSet(viewsets.ModelViewSet):
    queryset = Satellite.objects.all()
    serializer_class = SatelliteSerializer

class MixedTechnologyView(APIView):
    def get(self, request):
        rockets = Rocket.objects.all()
        satellites = Satellite.objects.all()

        rocket_serializer = RocketSerializer(rockets, many=True)
        satellite_serializer = SatelliteSerializer(satellites, many=True)

        mixed_data = rocket_serializer.data + satellite_serializer.data
        return Response(mixed_data)
