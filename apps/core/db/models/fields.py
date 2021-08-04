"""
created by Nagaj at 04/08/2021
"""
from django.db import models
from django.core import validators
from django.utils.translation import gettext_lazy as _


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