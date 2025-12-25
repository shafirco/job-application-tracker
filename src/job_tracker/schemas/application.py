"""Pydantic schemas for job application requests and responses."""

from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class ApplicationBase(BaseModel):
    """Base schema with common application fields."""
    company_name: str = Field(..., description="Name of the company")
    position: str = Field(..., description="Job position title")
    status: str = Field(..., description="Application status")
    applied_date: date = Field(..., description="Date when application was submitted")
    notes: Optional[str] = Field(None, description="Additional notes about the application")

class ApplicationCreate(ApplicationBase):
    """Schema for creating a new job application."""
    pass

class ApplicationUpdate(BaseModel):
    """Schema for updating an existing job application (partial updates)."""
    company_name: Optional[str] = Field(None, description="Name of the company")
    position: Optional[str] = Field(None, description="Job position title")
    status: Optional[str] = Field(None, description="Application status")
    applied_date: Optional[date] = Field(None, description="Date when application was submitted")
    notes: Optional[str] = Field(None, description="Additional notes about the application")

class ApplicationResponse(ApplicationBase):
    """Schema for job application responses (includes ID)."""
    id: int = Field(..., description="Unique identifier for the application")
    
    class Config:
        from_attributes = True
