from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "cars/index.html"

    def get_context_data(self, **kwargs):
        kwargs["open_countries"] = {
            "egypt": {"capital": "Cairo", "population": "100M"},
            "tunis": {"capital": "Tunis", "population": "20M"},

        }
        return kwargs


class AboutView(TemplateView):
    template_name = 'cars/about.html'


class ServicesView(TemplateView):
    template_name = 'cars/services.html'


class CarsView(TemplateView):
    template_name = 'cars/listcars.html'
