"""
created by Nagaj at 09/08/2021
"""
import re
from django.core.exceptions import ValidationError


def validate_vin_no(value):
    vin = re.findall(r"^[A-HJ-NPR-Z0-9]{17}$", value, flags=re.IGNORECASE)
    if vin:
        return vin[0]
    raise ValidationError(f"Invalid VIN number")
