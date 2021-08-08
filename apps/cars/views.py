import logging
from django.views.generic import TemplateView
from apps.teams.models import Team
from apps.cars.models import Car


class IndexView(TemplateView):
    template_name = "cars/index.html"
    MEMBERS_LIMIT = 4

    def get_context_data(self, **kwargs):
        kwargs["team"] = Team.objects.limit_team_by(limit=self.MEMBERS_LIMIT)
        logging.info(f"MEMBERS TEAM [{kwargs['team']}]")
        kwargs["features_cars"] = Car.objects.features_cars()
        logging.info(f"FEATURES CARS [{kwargs['features_cars']}]")
        kwargs["recently_cars"] = Car.objects.recently_cars()
        logging.info(f"RECENTLY CARS [{kwargs['recently_cars']}]")
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

    def get_context_data(self, **kwargs):
        kwargs["cars"] = Car.objects.all_cars()
        logging.info(f"CARS [{kwargs['cars']}]")
        return kwargs
