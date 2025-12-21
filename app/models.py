from sqlalchemy import Column, Integer, String, Date, Text
from app.database import Base

class Application(Base):
    """SQLAlchemy model for job applications"""
    __tablename__ = "applications"
    
    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String, nullable=False)
    position = Column(String, nullable=False)
    status = Column(String, nullable=False)
    applied_date = Column(Date, nullable=False)
    notes = Column(Text, nullable=True)
