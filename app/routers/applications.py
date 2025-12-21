from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import ApplicationCreate, ApplicationResponse
from app.database import get_db
from app.models import Application

# Create router for job application endpoints
router = APIRouter()

@router.post("/", response_model=ApplicationResponse)
def create_application(application: ApplicationCreate, db: Session = Depends(get_db)):
    """Create a new job application"""
    db_application = Application(
        company_name=application.company_name,
        position=application.position,
        status=application.status,
        applied_date=application.applied_date,
        notes=application.notes
    )
    
    db.add(db_application)
    db.commit()
    db.refresh(db_application)
    
    return db_application

@router.get("/", response_model=list[ApplicationResponse])
def get_applications(db: Session = Depends(get_db)):
    """Get all job applications"""
    applications = db.query(Application).all()
    return applications

@router.put("/{id}", response_model=ApplicationResponse)
def update_application(id: int, application: ApplicationCreate, db: Session = Depends(get_db)):
    """Update an existing job application"""
    db_application = db.query(Application).filter(Application.id == id).first()
    
    if not db_application:
        raise HTTPException(status_code=404, detail="Application not found")
    
    db_application.company_name = application.company_name
    db_application.position = application.position
    db_application.status = application.status
    db_application.applied_date = application.applied_date
    db_application.notes = application.notes
    
    db.commit()
    db.refresh(db_application)
    
    return db_application

@router.delete("/{id}")
def delete_application(id: int, db: Session = Depends(get_db)):
    """Delete a job application"""
    db_application = db.query(Application).filter(Application.id == id).first()
    
    if not db_application:
        raise HTTPException(status_code=404, detail="Application not found")
    
    db.delete(db_application)
    db.commit()
    
    return {"message": "Application deleted successfully"}
