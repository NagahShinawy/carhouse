"""
created by Nagaj at 06/08/2021
"""


from django.db import models
from django.db.models import Q


class CarManager(models.Manager):

    TOP_RECENTLY_ADDED = 8

    def all_cars(self) -> models.QuerySet:
        return super().all()

    def first_car_by_id(self, pk):
        car = super().filter(id=pk)
        if car:
            return car.first()
        return None

    def limit_car_by(self, limit):
        return self.all_cars()[:limit]

    def features_cars(self):
        return super().filter(is_features=True)

    def recently_cars(self):
        return self.all_cars().order_by("-created")[: self.TOP_RECENTLY_ADDED]

    def search_car(self, **kwargs):
        return super().filter(**kwargs).order_by("-created")

    def search_by_name_or_description(self, title, description):
        return super().filter(Q(car_title__icontains=title) | Q(description__icontains=description))
