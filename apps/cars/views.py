import logging
from django.views.generic import TemplateView
from apps.teams.models import Team


class IndexView(TemplateView):
    template_name = "cars/index.html"
    MEMBERS_LIMIT = 4

    def get_context_data(self, **kwargs):
        # kwargs["member"] = Team.objects.first_member_by_id(pk=257)
        kwargs["team"] = Team.objects.limit_team_by(limit=self.MEMBERS_LIMIT)
        logging.info(f"members team [{kwargs['team']}]")
        return kwargs


class AboutView(TemplateView):
    template_name = "cars/about.html"


class ServicesView(TemplateView):
    template_name = "cars/services.html"


class CarsView(TemplateView):
    template_name = "cars/listcars.html"
