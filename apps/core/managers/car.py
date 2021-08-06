"""
created by Nagaj at 06/08/2021
"""


from django.db import models


class CarManager(models.Manager):
    def all_cars(self) -> models.QuerySet:
        return super().all()

    def first_car_by_id(self, pk):
        car = super().filter(id=pk)
        if car:
            return car.first()
        return None

    def limit_car_by(self, limit):
        return self.all_cars()[:limit]
