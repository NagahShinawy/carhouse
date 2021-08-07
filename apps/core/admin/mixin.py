"""
created by Nagaj at 07/08/2021
"""

from django.utils.html import format_html


class ThumbnailMixin:
    CIRCLE = "50%"
    HREF_IMG_TAG = """
        <img src="{src}" width=30 height=30 style="border-radius:{border_radius}">
        """

    def thumbnail(self, obj):
        if obj.image:
            return format_html(
                self.HREF_IMG_TAG.format(
                    src=obj.image.url, href=obj.image.url, border_radius=self.CIRCLE
                )
            )
    thumbnail.short_description = "Photo"  # update col name in the admin
