from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from app.schemas import ApplicationCreate, ApplicationResponse
from app.database import get_db
from app.models import Application

# Create router for job application endpoints
router = APIRouter()

@router.post("/", response_model=ApplicationResponse)
def create_application(application: ApplicationCreate, db: Session = Depends(get_db)):
    """Create a new job application"""
    # Create SQLAlchemy model instance
    db_application = Application(
        company_name=application.company_name,
        position=application.position,
        status=application.status,
        applied_date=application.applied_date,
        notes=application.notes
    )
    
    # Add to database session
    db.add(db_application)
    db.commit()
    db.refresh(db_application)
    
    return db_application

@router.get("/", response_model=list[ApplicationResponse])
def get_applications(db: Session = Depends(get_db)):
    """Get all job applications"""
    applications = db.query(Application).all()
    return applications
