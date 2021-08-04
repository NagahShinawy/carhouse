from django.views.generic import TemplateView


class Contactus(TemplateView):
    template_name = "contacts/contact-us.html"
