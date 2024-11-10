from django.contrib import admin
from .models import Rocket, Satellite

@admin.register(Rocket)
class RocketAdmin(admin.ModelAdmin):
    list_display = ('name', 'height', 'diameter', 'mass', 'stages', 'first_flight', 'country')
    search_fields = ['name', 'country']
    list_filter = ['country', 'stages', 'first_flight']

    def get_field_queryset(self, db, model_field):
        if model_field.name == 'rocket':
            return model_field.remote_field.model.objects.all()
        return super().get_field_queryset(db, model_field)


@admin.register(Satellite)
class SatelliteAdmin(admin.ModelAdmin):
    list_display = ('name', 'mission_type', 'launch_date', 'orbit_type', 'rocket')
    search_fields = ['name', 'mission_type', 'orbit_type']
    list_filter = ['launch_date', 'orbit_type', 'rocket']

    def get_field_queryset(self, db, model_field):
        if model_field.name == 'rocket':
            return model_field.remote_field.model.objects.all()
        return super().get_field_queryset(db, model_field)
