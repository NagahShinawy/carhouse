from django.contrib import admin
from django.utils.html import format_html

from .models import Team
from apps.core.admin.mixin import ThumbnailMixin


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin, ThumbnailMixin):
    CIRCLE = "50%"
    HREF_IMG_TAG = """
    <img src="{src}" width=30 height=30 style="border-radius:{border_radius}">
    """
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

    def thumbnail(self, obj):
        return super().thumbnail(obj)
