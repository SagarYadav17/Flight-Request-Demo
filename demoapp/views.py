from django.shortcuts import render, redirect
import datetime

from demoapp.models import FlightRequest


def index(request):
    # Get all the flight requests order by id in descending order
    queryset = FlightRequest.objects.order_by("-id")
    return render(request, "index.html", {"flight_requests": queryset})


def request_flight(request):
    if request.method == "POST":
        # Get the number of flights requested
        number_of_flights = len(request.POST.getlist("aircraft_type"))

        # bulk create the flight requests
        flight_requests = []

        # Loop through the number of flights requested
        for i in range(number_of_flights):
            departure_datetime = f"{request.POST.getlist('departure_date')[i]} {request.POST.getlist('departure_time')[i]}"
            arrival_datetime = f"{request.POST.getlist('arrival_date')[i]} {request.POST.getlist('arrival_time')[i]}"

            # Create a new FlightRequest object
            flight_request = FlightRequest(
                aircraft_type=request.POST.getlist("aircraft_type")[i],
                origin=request.POST.getlist("origin")[i],
                destination=request.POST.getlist("destination")[i],
                departure_datetime=datetime.datetime.strptime(
                    departure_datetime, "%Y-%m-%d %H:%M"
                ),
                arrival_datetime=datetime.datetime.strptime(
                    arrival_datetime, "%Y-%m-%d %H:%M"
                ),
                flight_time=request.POST.getlist("flight_time")[i],
            )
            # Append the flight request to the list
            flight_requests.append(flight_request)

        # Bulk create the flight requests
        FlightRequest.objects.bulk_create(flight_requests)

    return redirect("index")
