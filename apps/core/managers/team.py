"""
created by Nagaj at 06/08/2021
"""
from django.db import models


class TeamManager(models.Manager):
    def all_team(self) -> models.QuerySet:
        return super().all()

    def first_member_by_id(self, pk):
        member = super().filter(id=pk)
        if member:
            return member.first()
        return None
