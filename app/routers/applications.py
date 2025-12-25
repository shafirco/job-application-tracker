from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.schemas import ApplicationCreate, ApplicationResponse
from app.database import get_db
from app.models import Application

# Create router for job application endpoints
router = APIRouter()

@router.post("/", response_model=ApplicationResponse)
async def create_application(application: ApplicationCreate, db: AsyncSession = Depends(get_db)):
    """Create a new job application"""
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

@router.get("/", response_model=list[ApplicationResponse])
async def get_applications(db: AsyncSession = Depends(get_db)):
    """Get all job applications"""
    result = await db.execute(select(Application))
    applications = result.scalars().all()
    return applications

@router.put("/{id}", response_model=ApplicationResponse)
async def update_application(id: int, application: ApplicationCreate, db: AsyncSession = Depends(get_db)):
    """Update an existing job application"""
    result = await db.execute(select(Application).where(Application.id == id))
    db_application = result.scalar_one_or_none()
    
    if not db_application:
        raise HTTPException(status_code=404, detail="Application not found")
    
    db_application.company_name = application.company_name
    db_application.position = application.position
    db_application.status = application.status
    db_application.applied_date = application.applied_date
    db_application.notes = application.notes
    
    await db.commit()
    await db.refresh(db_application)
    
    return db_application

@router.delete("/{id}")
async def delete_application(id: int, db: AsyncSession = Depends(get_db)):
    """Delete a job application"""
    result = await db.execute(select(Application).where(Application.id == id))
    db_application = result.scalar_one_or_none()
    
    if not db_application:
        raise HTTPException(status_code=404, detail="Application not found")
    
    await db.delete(db_application)
    await db.commit()
    
    return {"message": "Application deleted successfully"}
