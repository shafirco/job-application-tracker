from fastapi import APIRouter
from typing import List
from app.schemas import JobApplicationCreate, JobApplicationResponse

# Create router for job application endpoints
router = APIRouter()

# In-memory storage for job applications
applications_db = []
next_id = 1

@router.post("/", response_model=JobApplicationResponse)
def create_application(application: JobApplicationCreate):
    """Create a new job application"""
    global next_id
    
    # Create new application with generated ID
    new_application = JobApplicationResponse(
        id=next_id,
        **application.dict()
    )
    
    # Store in memory and increment ID counter
    applications_db.append(new_application)
    next_id += 1
    
    return new_application

@router.get("/", response_model=List[JobApplicationResponse])
def get_applications():
    """Get all job applications"""
    return applications_db
