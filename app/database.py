import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
load_dotenv()

# Get database URL from environment variables
DATABASE_URL = os.getenv("DATABASE_URL")

# Create async SQLAlchemy engine
engine = create_async_engine(DATABASE_URL)

# Create AsyncSessionLocal class for database sessions
AsyncSessionLocal = async_sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

# Create Base class for declarative models
Base = declarative_base()

# Dependency function to get async database session
async def get_db():
    """Dependency that provides an async database session"""
    async with AsyncSessionLocal() as session:
        yield session
