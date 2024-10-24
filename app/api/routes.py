# app/api/routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app.models import MaritimeReport
from pydantic import BaseModel
from typing import List

router = APIRouter()

class ReportSchema(BaseModel):
    coordinates: str
    issue: str
    rag_context: str

    class Config:
        from_attributes = True  # Changed from orm_mode to from_attributes

@router.get("/reports", response_model=List[ReportSchema])
def get_reports(db: Session = Depends(get_db)):
    reports = db.query(MaritimeReport).all()
    return reports

@router.post("/reports", response_model=ReportSchema)
def add_report(report: ReportSchema, db: Session = Depends(get_db)):
    new_report = MaritimeReport(
        coordinates=report.coordinates,
        issue=report.issue,
        rag_context=report.rag_context
    )
    db.add(new_report)
    db.commit()
    db.refresh(new_report)
    return new_report
