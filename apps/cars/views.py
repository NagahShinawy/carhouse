import logging
from django.views.generic import TemplateView
from apps.teams.models import Team


class IndexView(TemplateView):
    template_name = "cars/index.html"

    def get_context_data(self, **kwargs):
        kwargs["member"] = Team.objects.first_member_by_id(pk=257)
        logging.info(f"member team [{kwargs['member']}]")
        return kwargs


class AboutView(TemplateView):
    template_name = "cars/about.html"


class ServicesView(TemplateView):
    template_name = "cars/services.html"


class CarsView(TemplateView):
    template_name = "cars/listcars.html"
