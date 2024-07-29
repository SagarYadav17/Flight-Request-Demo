from django.contrib import admin

from demoapp.models import FlightRequest


@admin.register(FlightRequest)
class FlightRequestAdmin(admin.ModelAdmin):
    list_display = (
        "aircraft_type",
        "origin",
        "destination",
        "departure_datetime",
        "arrival_datetime",
        "flight_time",
    )
    search_fields = ("origin", "destination")
    list_filter = ("origin", "destination")
    date_hierarchy = "departure_datetime"
