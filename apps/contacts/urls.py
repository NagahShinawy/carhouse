"""
created by Nagaj at 02/08/2021
"""

from django.urls import path
from .views import Contactus

app_name = "contacts"

urlpatterns = [
    path("contact-us", Contactus.as_view(), name="contact-us"),
]