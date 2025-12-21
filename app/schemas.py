from enum import Enum
from pydantic import BaseModel
from datetime import date
from typing import Optional

# Enum for application status
class ApplicationStatus(str, Enum):
    applied = "Applied"
    interview = "Interview"
    offer = "Offer"
    rejected = "Rejected"

# Base schema for job application
class JobApplicationBase(BaseModel):
    company_name: str
    position: str
    status: ApplicationStatus
    applied_date: date
    notes: Optional[str] = None

# Schema for creating a job application
class JobApplicationCreate(JobApplicationBase):
    pass

# Schema for job application response (includes id)
class JobApplicationResponse(JobApplicationBase):
    id: int
