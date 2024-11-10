from django.contrib import admin
from .models import FlightSchedule

@admin.register(FlightSchedule)
class FlightScheduleAdmin(admin.ModelAdmin):
    list_display = ('mission_name', 'launch_date', 'destination', 'status')
    search_fields = ['mission_name', 'destination']
