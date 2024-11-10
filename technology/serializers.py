from django.conf import settings
from rest_framework import serializers
from .models import Rocket, Satellite

class RocketSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Rocket
        fields = ['id', 'name', 'description', 'height', 'diameter', 'mass', 'stages', 'first_flight', 'country', 'image']

    def get_image(self, obj):
        if obj.image:
            return settings.BASE_URL + obj.image.url
        return None

class SatelliteSerializer(serializers.ModelSerializer):
    rocket = serializers.PrimaryKeyRelatedField(queryset=Rocket.objects.all())
    image = serializers.SerializerMethodField()  # Используем SerializerMethodField для изображения

    class Meta:
        model = Satellite
        fields = ['id', 'name', 'description', 'mission_type', 'launch_date', 'orbit_type', 'rocket', 'image']

    def get_image(self, obj):
        if obj.image:
            return settings.BASE_URL + obj.image.url  # Добавляем BASE_URL к пути изображения
        return None
