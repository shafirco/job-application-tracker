"""Job application API endpoints."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List

from ...schemas.application import ApplicationCreate, ApplicationResponse, ApplicationUpdate
from ...models.application import Application
from ...core.database import get_db

router = APIRouter()

@router.post("/", response_model=ApplicationResponse, summary="Create Application")
async def create_application(
    application: ApplicationCreate, 
    db: AsyncSession = Depends(get_db)
) -> ApplicationResponse:
    """Create a new job application."""
    db_application = Application(
        company_name=application.company_name,
        position=application.position,
        status=application.status,
        applied_date=application.applied_date,
        notes=application.notes
    )
    
    db.add(db_application)
    await db.commit()
    await db.refresh(db_application)
    
    return db_application

@router.get("/", response_model=List[ApplicationResponse], summary="Get Applications")
async def get_applications(db: AsyncSession = Depends(get_db)) -> List[ApplicationResponse]:
    """Get all job applications."""
    result = await db.execute(select(Application))
    applications = result.scalars().all()
    return applications

@router.put("/{application_id}", response_model=ApplicationResponse, summary="Update Application")
async def update_application(
    application_id: int,
    application: ApplicationUpdate,
    db: AsyncSession = Depends(get_db)
) -> ApplicationResponse:
    """Update an existing job application (partial updates supported)."""
    result = await db.execute(select(Application).where(Application.id == application_id))
    db_application = result.scalar_one_or_none()
    
    if not db_application:
        raise HTTPException(status_code=404, detail="Application not found")
    
    # Update only provided fields
    update_data = application.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_application, field, value)
    
    await db.commit()
    await db.refresh(db_application)
    
    return db_application

@router.delete("/{application_id}", summary="Delete Application")
async def delete_application(
    application_id: int,
    db: AsyncSession = Depends(get_db)
) -> dict:
    """Delete a job application."""
    result = await db.execute(select(Application).where(Application.id == application_id))
    db_application = result.scalar_one_or_none()
    
    if not db_application:
        raise HTTPException(status_code=404, detail="Application not found")
    
    await db.delete(db_application)
    await db.commit()
    
    return {"message": "Application deleted successfully"}
