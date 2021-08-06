"""
created by Nagaj at 04/08/2021
"""
from datetime import date

from django.core import validators
from django.db import models
from django.utils.translation import gettext_lazy as _


def get_current_year():
    return date.year


class EmployeeIDField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 10
        kwargs["validators"] = [
            validators.MinLengthValidator(10),
            validators.RegexValidator(
                r"[0-9]", message=_("Only ASCII numbers are allowed")
            ),
        ]
        super(EmployeeIDField, self).__init__(*args, **kwargs)

    def __str__(self):
        return super(EmployeeIDField, self).__str__()


class YearField(models.IntegerField):

    MIN_YEAR = 1950
    MAX_YEAR = get_current_year()

    def __init__(self, *args, **kwargs):
        kwargs["validators"] = [
            validators.MinValueValidator(self.MIN_YEAR),
            validators.MaxValueValidator(
                2021, message=_("Only Year from are allowed")
            ),
        ]
        kwargs["default"] = get_current_year()
        super(YearField, self).__init__(*args, **kwargs)

    def __str__(self):
        return super(YearField, self).__str__()
