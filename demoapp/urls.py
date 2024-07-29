from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("request-flight/", views.request_flight, name="request-flight"),
]
