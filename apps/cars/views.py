import logging
from django.views.generic import TemplateView
from apps.teams.models import Team
from apps.cars.models import Car


class IndexView(TemplateView):
    template_name = "cars/index.html"
    MEMBERS_LIMIT = 4

    def get_context_data(self, **kwargs):
        kwargs["team"] = Team.objects.limit_team_by(limit=self.MEMBERS_LIMIT)
        kwargs["cars"] = Car.objects
        logging.info(f"members team [{kwargs['team']}]")
        logging.info(f"cars [{kwargs['cars']}]")
        return kwargs


class AboutView(TemplateView):
    template_name = "cars/about.html"
    MEMBERS_LIMIT = 3

    def get_context_data(self, **kwargs):
        kwargs["team"] = Team.objects.limit_team_by(limit=self.MEMBERS_LIMIT)
        logging.info(f"members team [{kwargs['team']}]")
        return kwargs


class ServicesView(TemplateView):
    template_name = "cars/services.html"


class CarsView(TemplateView):
    template_name = "cars/listcars.html"
