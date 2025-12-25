"""API dependencies - database sessions, auth, etc."""

from ..core.database import get_db

# Re-export for API use
__all__ = ["get_db"]
