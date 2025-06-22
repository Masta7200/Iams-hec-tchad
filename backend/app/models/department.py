from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base

class Department(Base):
    __tablename__ = "departments"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    code = Column(String, unique=True, nullable=False)  # e.g., "CS" for Computer Science
    description = Column(Text, nullable=True)
    head_of_department = Column(String, nullable=True)
    
    # Foreign key to faculty
    faculty_id = Column(Integer, ForeignKey("faculties.id"), nullable=False)
    
    # Relationship
    faculty = relationship("Faculty", backref="departments")
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())