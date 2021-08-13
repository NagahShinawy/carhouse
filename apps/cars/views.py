import logging
from django.views.generic import TemplateView, DetailView, ListView
from django.http import QueryDict
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
        logging.info(f"TEAM MEMBERS [{kwargs['team']}]")
        return kwargs


class ServicesView(TemplateView):
    template_name = "cars/services.html"


class CarListView(ListView):
    template_name = "cars/listcars.html"
    model = Car
    context_object_name = "cars"
    paginate_by = 10


class CarDetailView(DetailView):
    template_name = "cars/car-details.html"
    model = Car


class CarSearchView(ListView):
    template_name = "cars/search.html"
    model = Car
    queryset = Car.objects.none()
    context_object_name = "cars"

    @staticmethod
    def ger_query_params(params: QueryDict) -> dict:
        parsed_params = dict()
        brand = params.get("brand")
        make = params.get("make")
        location = params.get("location")
        year = params.get("year")
        type_ = params.get("type")
        transmission = params.get("transmission")
        price_range = params.get("price")
        if brand:
            parsed_params["brand__icontains"] = brand

        if make:
            parsed_params["make__icontains"] = make

        if location:
            parsed_params["location__icontains"] = location

        if year:
            parsed_params["year"] = year

        if type_:
            parsed_params["type__icontains"] = type_

        if transmission:
            parsed_params["transmission__icontains"] = transmission

        if price_range:
            parsed_params["price"] = price_range

        return parsed_params

    def get_queryset(self):
        title = self.request.GET.get("name")
        car_title = title if title else ""
        description = car_title
        cars = Car.objects.search_by_name_or_description(car_title, description)

        parsed_params = self.ger_query_params(self.request.GET)  # todo: optimized this
        if parsed_params or title:
            cars = cars.filter(**parsed_params)
        else:
            cars = Car.objects.all_cars()

        logging.info(f"Getting search car(s) {cars}")
        return cars
