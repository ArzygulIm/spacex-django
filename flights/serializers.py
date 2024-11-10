from rest_framework import serializers
from .models import FlightSchedule
from technology.models import Rocket, Satellite


class FlightScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightSchedule
        fields = ['id', 'mission_name', 'launch_date', 'rocket', 'satellite', 'destination', 'status']

    def create(self, validated_data):
        rocket_data = validated_data.pop('rocket', None)
        satellite_data = validated_data.pop('satellite', None)

        flight_schedule = FlightSchedule.objects.create(**validated_data)

        if rocket_data:
            flight_schedule.rocket = Rocket.objects.get(id=rocket_data.id)
        if satellite_data:
            flight_schedule.satellite = Satellite.objects.get(id=satellite_data.id)

        flight_schedule.save()
        return flight_schedule
