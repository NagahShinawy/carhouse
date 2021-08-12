from datetime import datetime
from apps.cars.models import Transmission, Location, Type, Use, Make, Brand


START_YEAR = 2000
current_year = datetime.today().year


def get_brands(request):
    return {"brands": [brand[-1] for brand in Brand.choices]}


def get_makes(request):
    return {"makes": [make[-1] for make in Make.choices]}


def get_years_range(request):
    return {"years": range(START_YEAR, current_year + 1)}


def get_transmissions(request):
    return {
        "transmissions": [transmission[-1] for transmission in Transmission.choices]
    }


def get_locations(request):
    return {"locations": [location[-1] for location in Location.choices]}


def car_type(request):
    return {"types": [ctype[-1] for ctype in Type.choices]}


def get_uses(request):
    return {"uses": [use[-1] for use in Use.choices]}
