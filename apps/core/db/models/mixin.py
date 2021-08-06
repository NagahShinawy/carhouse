"""
created by Nagaj at 04/08/2021
"""
import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _


def model_directory(instance, filename):
    return (
        f"{instance.__class__.__name__.lower()}/"
        f"{datetime.date.today().year}/"
        f"{datetime.date.today().month}/{filename}"
    )


class CreatedModelMixin(models.Model):
    created = models.DateTimeField(
        auto_now_add=True, verbose_name=_("created datetime")
    )

    class Meta:
        abstract = True


class ModifiedModelMixin(models.Model):
    modified = models.DateTimeField(
        auto_now=True, verbose_name=_("last modified datetime")
    )

    class Meta:
        abstract = True


class TimeStampModelMixin(models.Model):
    created = models.DateTimeField(
        auto_now_add=True, verbose_name=_("created datetime")
    )
    modified = models.DateTimeField(
        auto_now=True, verbose_name=_("last modified datetime")
    )

    class Meta:
        abstract = True


class ImageModelMixin(models.Model):
    image = models.ImageField(
        upload_to=model_directory, blank=True, null=True, verbose_name=_("image")
    )

    class Meta:
        abstract = True


class FullNameModelMixin(models.Model):
    fname = models.CharField(max_length=255, verbose_name=_("fname"))
    lname = models.CharField(max_length=255, verbose_name=_("lname"))

    class Meta:
        abstract = True
        ordering = ["fname"]  # todo: fix this not applied

    def __str__(self):
        return self.fname


class SocialMediaModelMixin(models.Model):
    fb = models.URLField(null=True, blank=True, verbose_name=_("facebook"))
    twitter = models.URLField(null=True, blank=True, verbose_name=_("twitter"))
    google = models.URLField(null=True, blank=True, verbose_name=_("google"))
    linkedin = models.URLField(null=True, blank=True, verbose_name=_("linkedin"))

    class Meta:
        abstract = True
