"""Job application API endpoints."""

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from ...schemas.application import ApplicationCreate, ApplicationResponse, ApplicationUpdate
from ...core.database import get_db
from ...services.application import ApplicationService

router = APIRouter()

@router.post("/", response_model=ApplicationResponse, summary="Create Application")
async def create_application(
    application: ApplicationCreate, 
    db: AsyncSession = Depends(get_db)
) -> ApplicationResponse:
    """Create a new job application."""
    return await ApplicationService.create_application(db, application)

@router.get("/", response_model=List[ApplicationResponse], summary="Get Applications")
async def get_applications(db: AsyncSession = Depends(get_db)) -> List[ApplicationResponse]:
    """Get all job applications."""
    return await ApplicationService.get_all_applications(db)

@router.put("/{application_id}", response_model=ApplicationResponse, summary="Update Application")
async def update_application(
    application_id: int,
    application: ApplicationUpdate,
    db: AsyncSession = Depends(get_db)
) -> ApplicationResponse:
    """Update an existing job application (partial updates supported)."""
    return await ApplicationService.update_application(db, application_id, application)

@router.delete("/{application_id}", summary="Delete Application")
async def delete_application(
    application_id: int,
    db: AsyncSession = Depends(get_db)
) -> dict:
    """Delete a job application."""
    await ApplicationService.delete_application(db, application_id)
    return {"message": "Application deleted successfully"}
