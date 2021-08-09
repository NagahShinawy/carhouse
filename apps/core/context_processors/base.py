"""
created by Nagaj at 09/08/2021
"""

EMAIL = "info@opensooq.com"
WEBSITE = "www.opensooq.com"
FAX = "+0477 85X6 552"
PHONE = "966 7810 000"
WORKING_HOURS = "Mon - Sun: 8:00am - 6:00pm"


def email(request):
    return {"email": EMAIL}


def website(request):
    return {"website": WEBSITE}


def phone(request):
    return {"phone": PHONE}


def fax(request):
    return {"fax": FAX}


def working_hours(request):
    return {"working_hours": WORKING_HOURS}


def car_urls(request):
    pass
