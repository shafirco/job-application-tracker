from fastapi import FastAPI
from app.routers import applications
from app.database import Base, engine
from app import models

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Job Application Tracker API")

# Include routers
app.include_router(applications.router, prefix="/applications", tags=["Applications"])

@app.get("/")
def read_root():
    return {"message": "Job Application Tracker API is running"}
