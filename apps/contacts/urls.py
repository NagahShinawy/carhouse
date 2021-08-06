"""
created by Nagaj at 02/08/2021
"""

from django.urls import path
from .views import ContactusView

app_name = "contacts"

urlpatterns = [
    path("contact-us/", ContactusView.as_view(), name="contact-us"),
]
