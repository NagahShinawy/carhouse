"""
created by Nagaj at 02/08/2021
"""

from django.urls import path
from .views import home

app_name = "cars"

urlpatterns = [
    path("", home, name="home"),
]