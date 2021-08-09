"""
created by Nagaj at 09/08/2021
"""
import re
from django.core.exceptions import ValidationError


def validate_vin_no(value):
    vin = re.findall(r"^[A-HJ-NPR-Z\\d]{8}[\\dX][A-HJ-NPR-Z\\d]{2}\\d{6}$", value)
    if vin:
        return vin[0]
    raise ValidationError(f"Invalid vin no {value}")
