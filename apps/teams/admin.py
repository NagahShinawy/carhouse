from django.contrib import admin
from django.utils.html import format_html

from .models import Team
from apps.core.admin.mixin import ThumbnailMixin


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin, ThumbnailMixin):
    CIRCLE = "50px"
    list_display = (
        "id",
        "thumbnail",
        "emp_id",
        "fname",
        "lname",
        "created",
        "modified",
    )
    list_display_links = ("id", "thumbnail", "emp_id")
    list_per_page = 10
    search_fields = ("id", "emp_id", "fname", "lname", "position")
    list_filter = ("created", "modified", "position")
    # raw_id_fields = ("emp_id",)
    # list_select_related = ("nationality",)

    def thumbnail(self, obj, *args):
        return super().thumbnail(obj, is_link=True)
