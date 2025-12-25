"""Database configuration and session management."""

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .config import settings

# Create async SQLAlchemy engine
engine = create_async_engine(settings.database_url)

# Create AsyncSessionLocal class for database sessions
AsyncSessionLocal = async_sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

# Create Base class for declarative models
Base = declarative_base()

# Dependency function to get async database session
async def get_db():
    """Dependency that provides an async database session."""
    async with AsyncSessionLocal() as session:
        yield session
