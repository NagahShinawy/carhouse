"""
created by Nagaj at 02/08/2021
"""

from django.urls import path
from .views import ContactusView, SignUpView, DashboardView, LogoutView, LoginView

app_name = "contacts"

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path("contact-us/", ContactusView.as_view(), name="contact-us"),
]
