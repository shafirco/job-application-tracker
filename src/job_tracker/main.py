"""Main FastAPI application factory."""

from fastapi import FastAPI
from contextlib import asynccontextmanager

from .core.config import settings
from .core.database import Base, engine
from .api.v1 import applications_router
from . import models  # Import to register models

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan - startup and shutdown events."""
    # Create database tables on startup
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    app = FastAPI(
        title=settings.project_name,
        version=settings.version,
        lifespan=lifespan,
        openapi_url=f"{settings.api_v1_prefix}/openapi.json",
        docs_url="/docs",
        redoc_url="/redoc"
    )

    # Include API routers
    app.include_router(
        applications_router, 
        prefix=f"{settings.api_v1_prefix}/applications", 
        tags=["Applications"]
    )

    @app.get("/")
    async def read_root():
        """Health check endpoint."""
        return {
            "message": f"{settings.project_name} is running",
            "version": settings.version,
            "docs_url": "/docs"
        }

    return app

# Create app instance
app = create_app()
