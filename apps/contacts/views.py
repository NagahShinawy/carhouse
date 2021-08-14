from django.views.generic import TemplateView


class ContactusView(TemplateView):
    template_name = "contacts/contact-us.html"


class SignUpView(TemplateView):
    template_name = "contacts/signup.html"


class LoginView(TemplateView):
    template_name = "contacts/login.html"
