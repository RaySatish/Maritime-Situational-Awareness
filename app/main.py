# app/main.py
from fastapi import FastAPI
from app.api.routes import router as api_router
from app.db import Base, engine


# Create database tables if they don't exist
Base.metadata.create_all(bind=engine)

# Initialize FastAPI
app = FastAPI(title="Maritime Situational Awareness API")

# Include API routes
app.include_router(api_router, prefix="/api/v1")

# Run the app using: uvicorn app.main:app --reload
