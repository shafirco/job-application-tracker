"""Application configuration settings."""

import os
from typing import Optional
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    """Application settings from environment variables."""
    
    # Database
    database_url: str = os.getenv(
        "DATABASE_URL", 
        "postgresql+psycopg://postgres:password@localhost:5432/jobtracker"
    )
    
    # API
    api_v1_prefix: str = "/api/v1"
    project_name: str = "Job Application Tracker API"
    version: str = "0.1.0"
    
    # Security
    secret_key: Optional[str] = os.getenv("SECRET_KEY")
    
    class Config:
        env_file = ".env"

settings = Settings()
