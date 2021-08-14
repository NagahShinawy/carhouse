from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.contrib.auth.views import LoginView as BaseLoginView
from django.urls import reverse


class ContactusView(TemplateView):
    template_name = "contacts/contact-us.html"


class SignUpView(TemplateView):
    template_name = "contacts/signup.html"


class LoginView(BaseLoginView):
    template_name = "contacts/login.html"


class LogoutView(BaseLogoutView):
    def get_next_page(self):
        return reverse("cars:index")


class DashboardView(TemplateView):
    template_name = "contacts/dashboard.html"
