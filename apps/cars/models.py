from datetime import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core import managers
from apps.core.db.models import (
    TimeStampModelMixin,
    ImageModelMixin,
)
from apps.core.db.models.mixin import model_directory


class State(models.TextChoices):
    ALABAMA = ('AL', 'Alabama')
    ALASKA = ('AK', 'Alaska')
    ARIZONA = ('AZ', 'Arizona')
    ARKANSAS = ('AR', 'Arkansas')
    CALIFORNIA = ('CA', 'California')
    COLORADO = ('CO', 'Colorado')
    CONNECTICUT = ('CT', 'Connecticut')
    DELAWARE = ('DE', 'Delaware')
    DISTRICT_OF_COLUMBIA = ('DC', 'District Of Columbia')
    FLORIDA = ('FL', 'Florida')
    GEORGIA = ('GA', 'Georgia')
    HAWAII = ('HI', 'Hawaii')
    IDAHO = ('ID', 'Idaho')
    ILLINOIS = ('IL', 'Illinois')
    INDIANA = ('IN', 'Indiana')
    IOWA = ('IA', 'Iowa')
    KANSAS = ('KS', 'Kansas')
    KENTUCKY = ('KY', 'Kentucky')
    LOUISIANA = ('LA', 'Louisiana')
    MAINE = ('ME', 'Maine')
    MARYLAND = ('MD', 'Maryland')
    MASSACHUSETTS = ('MA', 'Massachusetts')
    MICHIGAN = ('MI', 'Michigan')
    MINNESOTA = ('MN', 'Minnesota')
    MISSISSIPPI = ('MS', 'Mississippi')
    MISSOURI = ('MO', 'Missouri')
    MONTANA = ('MT', 'Montana')
    NEBRASKA = ('NE', 'Nebraska')
    NEVADA = ('NV', 'Nevada')
    HAMPSHIRE = ('NH', 'New Hampshire')
    NEW_JERSEY = ('NJ', 'New Jersey')
    NEW_MEXICO = ('NM', 'New Mexico')
    NEW_YORK = ('NY', 'New York')
    NORTH_CAROLINA = ('NC', 'North Carolina')
    DAKOTA = ('ND', 'North Dakota')
    OHIO = ('OH', 'Ohio')
    OKLAHOMA = ('OK', 'Oklahoma')
    OREGON = ('OR', 'Oregon')
    PENNSYLVANIA = ('PA', 'Pennsylvania')
    ISLAND = ('RI', 'Rhode Island')
    SOUTH_CAROLINA = ('SC', 'South Carolina')
    SOUTH_DAKOTA = ('SD', 'South Dakota')
    TENNESSEE = ('TN', 'Tennessee')
    TEXAS = ('TX', 'Texas')
    UTAH = ('UT', 'Utah')
    VERMONT = ('VT', 'Vermont')
    VIRGINIA = ('VA', 'Virginia')
    WASHINGTON = ('WA', 'Washington')
    WEST_VIRGINIA = ('WV', 'West Virginia')
    WISCONSIN = ('WI', 'Wisconsin')
    WYOMING = ('WY', 'Wyoming')


class Features(models.TextChoices):
    CRUISE_CONTROL = ('Cruise Control', 'Cruise Control')
    AUDIO_INTERFACE = ('Audio Interface', 'Audio Interface')
    AIRBAGS = ('Airbags', 'Airbags')
    AIR_CONDITIONING = ('Air Conditioning', 'Air Conditioning')
    SEAT_HEATING = ('Seat Heating', 'Seat Heating')
    ALARM_SYSTEM = ('Alarm System', 'Alarm System')
    PARK_ASSIST = ('ParkAssist', 'ParkAssist')
    POWER_STEERING = ('Power Steering', 'Power Steering')
    REVERSING_CAMERA = ('Reversing Camera', 'Reversing Camera')
    DIRECT_FUEL_INJECTION = ('Direct Fuel Injection', 'Direct Fuel Injection')
    AUTO_START_STOP = ('Auto Start/Stop', 'Auto Start/Stop')
    WIND_DEFLECTOR = ('Wind Deflector', 'Wind Deflector')
    BLUETOOTH_HANDSET = ('Bluetooth Handset', 'Bluetooth Handset')


class Doors(models.IntegerChoices):
    UP_LEFT = 1, "1"
    UP_RIGHT = 2, "2"
    DOWN_LEFT = 3, "3"
    DOWN_RIGHT = 4, "4"


class Passengers(models.IntegerChoices):
    PASSENGER1 = 1, "1"
    PASSENGER2 = 2, "2"
    PASSENGER3 = 3, "3"
    PASSENGER4 = 4, "4"
    PASSENGER5 = 5, "5"
    PASSENGER6 = 6, "6"
    PASSENGER7 = 7, "7"
    PASSENGER8 = 8, "8"


class Fuel(models.TextChoices):
    gasoline = "gasoline", _("Gasoline")
    diesel = "diesel", _("Diesel")
    Bio = "bio", _("Bio")
    ethanol = "ethanol", _("Ethanol")


class Owner(models.IntegerChoices):

    @property
    def choices(self):
        return list(range(1, 101))


class Car(TimeStampModelMixin, ImageModelMixin, models.Model):

    MIX_YEAR = 2000

    year_choices = ((year, year) for year in [year for year in range(MIX_YEAR, datetime.now().year + 1)])

    car_title = models.CharField(max_length=255, verbose_name=_("car title"))

    state = models.CharField(choices=State.choices, verbose_name=_("state"), max_length=50)

    city = models.CharField(max_length=100, verbose_name=_("city"))

    color = models.CharField(max_length=100, verbose_name=_("color"))

    model = models.CharField(max_length=100, verbose_name=_("model"))

    year = models.PositiveSmallIntegerField(choices=year_choices, verbose_name=_("year"))

    conditions = models.CharField(max_length=100, verbose_name=_("conditions"))

    price = models.FloatField(verbose_name=_("price"))

    description = models.TextField(max_length=255, verbose_name=_("description"))

    image = models.ImageField(upload_to=model_directory, verbose_name=_("image"))

    image2 = models.ImageField(upload_to=model_directory, verbose_name=_("image2"), null=True, blank=True)

    image3 = models.ImageField(upload_to=model_directory, verbose_name=_("image3"), null=True, blank=True)

    image4 = models.ImageField(upload_to=model_directory, verbose_name=_("image4"), null=True, blank=True)

    image5 = models.ImageField(upload_to=model_directory, verbose_name=_("image5"), null=True, blank=True)

    features = models.CharField(max_length=100, choices=Features.choices, verbose_name=_("features"))

    body_style = models.CharField(max_length=100, verbose_name=_("body style"), default="")

    engine = models.CharField(max_length=100, verbose_name=_("engine"))

    transmission = models.CharField(max_length=100, verbose_name=_("transmission"))

    interior = models.CharField(max_length=100, verbose_name=_("interior"))

    miles = models.BigIntegerField(verbose_name=_("miles"))

    doors = models.PositiveSmallIntegerField(choices=Doors.choices, verbose_name=_("doors"))

    passengers = models.PositiveSmallIntegerField(choices=Passengers.choices, verbose_name=_("passengers"))

    vin_no = models.CharField(max_length=100, verbose_name=_("vin no"))

    mileages = models.BigIntegerField(verbose_name=_("mileage"))

    fuel_type = models.CharField(max_length=20, choices=Fuel.choices, verbose_name=_("fuel type"))

    no_of_owners = models.PositiveSmallIntegerField(choices=Owner.choices, verbose_name=_("number of owners"))

    is_features = models.BooleanField(default=False, verbose_name=_("features?"))

    objects = managers.CarManager()

    def __str__(self):
        return f"{self.car_title}-{self.model}-{self.price}"
