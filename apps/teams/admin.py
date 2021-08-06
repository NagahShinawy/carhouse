from django.contrib import admin

from .models import Team


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "emp_id",
        "fname",
        "lname",
        "image",
        "created",
        "modified",
    )
    list_display_links = ("id", "emp_id")
    list_per_page = 10
    search_fields = ("id", "emp_id", "fname", "lname", "position")
    list_filter = ("created", "modified")
    # raw_id_fields = ("emp_id",)
    # list_select_related = ("nationality",)
