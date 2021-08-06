from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.core import managers


from apps.core.db.models import (
    TimeStampModelMixin,
    FullNameModelMixin,
    ImageModelMixin,
    SocialMediaModelMixin,
    EmployeeIDField,
)


class Team(
    TimeStampModelMixin,
    FullNameModelMixin,
    ImageModelMixin,
    SocialMediaModelMixin,
    models.Model,
):
    emp_id = EmployeeIDField(verbose_name=_("employee id"))
    position = models.CharField(max_length=225)
    objects = managers.TeamManager()

    class Meta:
        verbose_name = "Team Person"
        ordering = ["-id"]

    def __str__(self):
        return f"#{self.id}-{self.emp_id}-{self.fname}"
