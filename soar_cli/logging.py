"""
logging.py
Sets up structlog + stdlib logging, driven by Settings.
"""
import logging
import structlog
from .settings import Settings

def configure_logging(settings: Settings):
    log_level = logging.getLevelName(settings.log_level.upper())
    handlers = [logging.StreamHandler()]

    logging.basicConfig(
        level=log_level,
        format="%(message)s",
        handlers=handlers,
    )

    structlog.configure(
        wrapper_class=structlog.make_filtering_bound_logger(log_level),
        processors=[
            structlog.processors.TimeStamper(fmt="%Y-%m-%d %H:%M:%S"),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            structlog.dev.ConsoleRenderer(),
        ],
    )
