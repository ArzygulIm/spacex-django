from rest_framework import viewsets
from .models import FlightSchedule
from .serializers import FlightScheduleSerializer

class FlightScheduleViewSet(viewsets.ModelViewSet):
    queryset = FlightSchedule.objects.all()
    serializer_class = FlightScheduleSerializer
