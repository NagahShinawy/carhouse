from django.views.generic import TemplateView


class ContactusView(TemplateView):
    template_name = "contacts/contact-us.html"
