from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.routers import applications
from app.database import Base, engine
from app import models

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create database tables on startup
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(title="Job Application Tracker API", lifespan=lifespan)

# Include routers
app.include_router(applications.router, prefix="/applications", tags=["Applications"])

@app.get("/")
async def read_root():
    return {"message": "Job Application Tracker API is running"}
