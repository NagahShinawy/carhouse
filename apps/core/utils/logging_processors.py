import logging
import threading
from typing import (
    List,
    Union,
)
from structlog.stdlib import BoundLogger

from sentry_sdk import add_breadcrumb
from structlog_sentry import SentryJsonProcessor


THREADLOCAL = threading.local()


def _ensure_threadlocal():
    if not hasattr(THREADLOCAL, "context"):
        THREADLOCAL.context = {}


def merge_in_threadlocal_processor(logger, method_name, event_dict):
    """A structlog processor that merges in a thread-local context"""

    _ensure_threadlocal()
    context = THREADLOCAL.context.copy()
    context.update(event_dict)
    return context


class LimitedThreadLocalBoundLogger(BoundLogger):
    """Extended logger class with utility thread local binding functions."""

    @staticmethod
    def clear_threadlocal():
        """Clear the thread-local context."""

        THREADLOCAL.context = {}

    @staticmethod
    def bind_threadlocal(**kwargs):
        """Put keys and values into the thread-local context."""

        _ensure_threadlocal()
        THREADLOCAL.context.update(kwargs)


class SentryBreadcrumbJsonProcessor(SentryJsonProcessor):
    def __init__(
        self,
        level: int = logging.WARNING,
        breadcrumb_level: int = logging.INFO,
        active: bool = True,
        as_extra: bool = True,
        tag_keys: Union[List[str], str] = None,
    ) -> None:
        self.breadcrumb_level = breadcrumb_level
        super().__init__(
            level=level, active=active, as_extra=as_extra, tag_keys=tag_keys,
        )

    def save_breadcrumb(self, logger, event_dict):
        data = event_dict.copy()
        data.pop("event")
        data.pop("logger", None)
        data.pop("level", None)
        data.pop("timestamp", None)
        breadcrumb = {
            "ty": "log",
            "level": event_dict["level"].lower(),
            "category": event_dict.get("logger") or logger.name,
            "message": event_dict["event"],
            "data": data,
        }
        add_breadcrumb(breadcrumb, hint={"event_dict": event_dict})

    def __call__(self, logger, method, event_dict) -> dict:
        do_breadcrumb = (
            getattr(logging, event_dict["level"].upper()) >= self.breadcrumb_level
        )

        if do_breadcrumb:
            self.save_breadcrumb(logger, event_dict)

        return super().__call__(logger=logger, method=method, event_dict=event_dict)
