"""Job Tracker API - A FastAPI application for tracking job applications."""

__version__ = "0.1.0"
__author__ = "Shafir Cohen"

# Export main objects for easy imports
from .main import create_app

__all__ = ["create_app"]
