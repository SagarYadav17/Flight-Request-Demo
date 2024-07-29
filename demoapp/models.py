from django.db import models


class FlightRequest(models.Model):
    aircraft_type = models.CharField(max_length=255)
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    departure_datetime = models.DateTimeField()
    arrival_datetime = models.DateTimeField()
    flight_time = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.id}"
