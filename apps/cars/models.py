from datetime import datetime

from django.db import models
from django.core import validators
from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField
from ckeditor.fields import RichTextField

from apps.core import managers
from apps.core.db.models import (
    TimeStampModelMixin,
    ImageModelMixin,
)
from apps.core.db.models.mixin import model_directory
from apps.core.utils import validators as _validator
from apps.core.db.models.fields import VinNumberField


class ChoiceManager:

    choices = ()


class State(models.TextChoices):
    ALABAMA = ("AL", "Alabama")
    ALASKA = ("AK", "Alaska")
    ARIZONA = ("AZ", "Arizona")
    ARKANSAS = ("AR", "Arkansas")
    CALIFORNIA = ("CA", "California")
    COLORADO = ("CO", "Colorado")
    CONNECTICUT = ("CT", "Connecticut")
    DELAWARE = ("DE", "Delaware")
    DISTRICT_OF_COLUMBIA = ("DC", "District Of Columbia")
    FLORIDA = ("FL", "Florida")
    GEORGIA = ("GA", "Georgia")
    HAWAII = ("HI", "Hawaii")
    IDAHO = ("ID", "Idaho")
    ILLINOIS = ("IL", "Illinois")
    INDIANA = ("IN", "Indiana")
    IOWA = ("IA", "Iowa")
    KANSAS = ("KS", "Kansas")
    KENTUCKY = ("KY", "Kentucky")
    LOUISIANA = ("LA", "Louisiana")
    MAINE = ("ME", "Maine")
    MARYLAND = ("MD", "Maryland")
    MASSACHUSETTS = ("MA", "Massachusetts")
    MICHIGAN = ("MI", "Michigan")
    MINNESOTA = ("MN", "Minnesota")
    MISSISSIPPI = ("MS", "Mississippi")
    MISSOURI = ("MO", "Missouri")
    MONTANA = ("MT", "Montana")
    NEBRASKA = ("NE", "Nebraska")
    NEVADA = ("NV", "Nevada")
    HAMPSHIRE = ("NH", "New Hampshire")
    NEW_JERSEY = ("NJ", "New Jersey")
    NEW_MEXICO = ("NM", "New Mexico")
    NEW_YORK = ("NY", "New York")
    NORTH_CAROLINA = ("NC", "North Carolina")
    DAKOTA = ("ND", "North Dakota")
    OHIO = ("OH", "Ohio")
    OKLAHOMA = ("OK", "Oklahoma")
    OREGON = ("OR", "Oregon")
    PENNSYLVANIA = ("PA", "Pennsylvania")
    ISLAND = ("RI", "Rhode Island")
    SOUTH_CAROLINA = ("SC", "South Carolina")
    SOUTH_DAKOTA = ("SD", "South Dakota")
    TENNESSEE = ("TN", "Tennessee")
    TEXAS = ("TX", "Texas")
    UTAH = ("UT", "Utah")
    VERMONT = ("VT", "Vermont")
    VIRGINIA = ("VA", "Virginia")
    WASHINGTON = ("WA", "Washington")
    WEST_VIRGINIA = ("WV", "West Virginia")
    WISCONSIN = ("WI", "Wisconsin")
    WYOMING = ("WY", "Wyoming")


class Features(models.TextChoices):
    CRUISE_CONTROL = ("Cruise Control", "Cruise Control")
    AUDIO_INTERFACE = ("Audio Interface", "Audio Interface")
    AIRBAGS = ("Airbags", "Airbags")
    AIR_CONDITIONING = ("Air Conditioning", "Air Conditioning")
    SEAT_HEATING = ("Seat Heating", "Seat Heating")
    ALARM_SYSTEM = ("Alarm System", "Alarm System")
    PARK_ASSIST = ("ParkAssist", "ParkAssist")
    POWER_STEERING = ("Power Steering", "Power Steering")
    REVERSING_CAMERA = ("Reversing Camera", "Reversing Camera")
    DIRECT_FUEL_INJECTION = ("Direct Fuel Injection", "Direct Fuel Injection")
    AUTO_START_STOP = ("Auto Start/Stop", "Auto Start/Stop")
    WIND_DEFLECTOR = ("Wind Deflector", "Wind Deflector")
    BLUETOOTH_HANDSET = ("Bluetooth Handset", "Bluetooth Handset")


class Doors(ChoiceManager):
    MAX_DOORS = 4
    choices = ((i, str(i)) for i in range(1, MAX_DOORS + 1))


class Passengers(ChoiceManager):
    MAX_PASSENGERS = 8
    choices = ((i, str(i)) for i in range(1, MAX_PASSENGERS + 1))


class Fuel(models.TextChoices):
    gasoline = "gasoline", _("Gasoline")
    diesel = "diesel", _("Diesel")
    Bio = "bio", _("Bio")
    ethanol = "ethanol", _("Ethanol")


class Owner(ChoiceManager):
    MAX_OWNERS = 10
    choices = ((i, str(i)) for i in range(1, MAX_OWNERS + 1))


class Year:
    MIX_YEAR = 2000

    @classmethod
    def choices(cls):
        return [
            (year, str(year))
            for year in [year for year in range(cls.MIX_YEAR, datetime.now().year + 1)]
        ]


class Transmission(models.TextChoices):
    manual = "manual", _("Manual")
    automatic = "automatic", _("Automatic")


class Car(TimeStampModelMixin, ImageModelMixin, models.Model):

    car_title = models.CharField(max_length=255, verbose_name=_("car title"))

    state = models.CharField(
        choices=State.choices, verbose_name=_("state"), max_length=50
    )

    city = models.CharField(max_length=100, verbose_name=_("city"))

    color = models.CharField(max_length=100, verbose_name=_("color"))

    model = models.CharField(max_length=100, verbose_name=_("model"))

    year = models.PositiveSmallIntegerField(
        choices=Year.choices(), verbose_name=_("year")
    )

    conditions = models.CharField(max_length=100, verbose_name=_("conditions"))

    price = models.FloatField(verbose_name=_("price"))

    description = RichTextField(max_length=255, verbose_name=_("description"))

    image = models.ImageField(upload_to=model_directory, verbose_name=_("image"))

    image2 = models.ImageField(
        upload_to=model_directory, verbose_name=_("image2"), null=True, blank=True
    )

    image3 = models.ImageField(
        upload_to=model_directory, verbose_name=_("image3"), null=True, blank=True
    )

    image4 = models.ImageField(
        upload_to=model_directory, verbose_name=_("image4"), null=True, blank=True
    )

    image5 = models.ImageField(
        upload_to=model_directory, verbose_name=_("image5"), null=True, blank=True
    )

    features = MultiSelectField(
        choices=Features.choices, blank=True, null=True, verbose_name=_("features")
    )

    body_style = models.CharField(
        max_length=100, verbose_name=_("body style"), default=""
    )

    engine = models.CharField(max_length=100, verbose_name=_("engine"))

    transmission = models.CharField(
        max_length=10,
        choices=Transmission.choices,
        default=Transmission.automatic,
        verbose_name=_("transmission"),
    )

    interior = models.CharField(max_length=100, verbose_name=_("interior"))

    miles = models.BigIntegerField(verbose_name=_("miles"))

    doors = models.PositiveSmallIntegerField(
        choices=Doors.choices, verbose_name=_("doors")
    )

    passengers = models.PositiveSmallIntegerField(
        choices=Passengers.choices, verbose_name=_("passengers")
    )

    vin_no = VinNumberField(verbose_name=_("VIN number"))
    mileages = models.BigIntegerField(verbose_name=_("mileage"))

    fuel_type = models.CharField(
        max_length=20, choices=Fuel.choices, verbose_name=_("fuel type")
    )

    no_of_owners = models.PositiveSmallIntegerField(
        choices=Owner.choices, verbose_name=_("number of owners")
    )

    is_features = models.BooleanField(default=False, verbose_name=_("features?"))

    discount = models.PositiveSmallIntegerField(
        default=0,
        validators=[validators.MinValueValidator(0), validators.MaxValueValidator(100)],
    )

    objects = managers.CarManager()

    def save(self, *args, **kwargs):
        setattr(self, "old_price", self.price)
        if self.discount > 0:
            discount = self.discount / 100
            self.price = self.price - (self.price * discount)
        super(Car, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.car_title}-{self.model}-{self.price}"

    class Meta:
        verbose_name = "list Car"
        ordering = ["-created"]
