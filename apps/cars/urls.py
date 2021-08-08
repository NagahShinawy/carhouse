"""
created by Nagaj at 02/08/2021
"""

from django.urls import path
from .views import IndexView, AboutView, ServicesView, CarsView, CarDetailView

app_name = "cars"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("about/", AboutView.as_view(), name="about"),
    path("services/", ServicesView.as_view(), name="services"),
    path("cars/", CarsView.as_view(), name="cars"),
    path("cars/<int:pk>", CarDetailView.as_view(), name="car-details"),
]
