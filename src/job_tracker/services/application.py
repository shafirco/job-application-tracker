"""Application service containing business logic."""

from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from fastapi import HTTPException

from ..models.application import Application
from ..schemas.application import ApplicationCreate, ApplicationUpdate


class ApplicationService:
    """Service class for job application business logic."""
    
    @staticmethod
    async def create_application(
        db: AsyncSession, 
        application_data: ApplicationCreate
    ) -> Application:
        """Create a new job application."""
        db_application = Application(
            company_name=application_data.company_name,
            position=application_data.position,
            status=application_data.status,
            applied_date=application_data.applied_date,
            notes=application_data.notes
        )
        
        db.add(db_application)
        await db.commit()
        await db.refresh(db_application)
        
        return db_application
    
    @staticmethod
    async def get_all_applications(db: AsyncSession) -> List[Application]:
        """Get all job applications."""
        result = await db.execute(select(Application))
        return result.scalars().all()
    
    @staticmethod
    async def get_application_by_id(db: AsyncSession, application_id: int) -> Application:
        """Get a specific application by ID."""
        result = await db.execute(select(Application).where(Application.id == application_id))
        db_application = result.scalar_one_or_none()
        
        if not db_application:
            raise HTTPException(status_code=404, detail="Application not found")
            
        return db_application
    
    @staticmethod
    async def update_application(
        db: AsyncSession, 
        application_id: int, 
        application_data: ApplicationUpdate
    ) -> Application:
        """Update an existing job application (partial updates supported)."""
        db_application = await ApplicationService.get_application_by_id(db, application_id)
        
        # Update only provided fields
        update_data = application_data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_application, field, value)
        
        await db.commit()
        await db.refresh(db_application)
        
        return db_application
    
    @staticmethod
    async def delete_application(db: AsyncSession, application_id: int) -> bool:
        """Delete a job application using optimized direct query."""
        # Use direct delete query for better performance
        result = await db.execute(
            delete(Application).where(Application.id == application_id)
        )
        
        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail="Application not found")
        
        await db.commit()
        return True
