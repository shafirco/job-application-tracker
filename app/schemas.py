from pydantic import BaseModel
from datetime import date
from typing import Optional

class ApplicationCreate(BaseModel):
    """Schema for creating applications"""
    company_name: str
    position: str
    status: str
    applied_date: date
    notes: Optional[str] = None

class ApplicationResponse(BaseModel):
    """Schema for application response"""
    id: int
    company_name: str
    position: str
    status: str
    applied_date: date
    notes: Optional[str] = None
    
    class Config:
        from_attributes = True
