# app/models.py
from sqlalchemy import Column, Integer, String, Text, DateTime
from .db import Base
import datetime

class MaritimeReport(Base):
    __tablename__ = "maritime_reports"

    id = Column(Integer, primary_key=True, index=True)
    coordinates = Column(String, index=True)
    issue = Column(Text)
    rag_context = Column(Text)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
