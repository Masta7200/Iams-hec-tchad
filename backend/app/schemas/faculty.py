from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class FacultyBase(BaseModel):
    name: str
    code: str
    description: Optional[str] = None
    dean_name: Optional[str] = None

class FacultyCreate(FacultyBase):
    pass

class FacultyUpdate(BaseModel):
    name: Optional[str] = None
    code: Optional[str] = None
    description: Optional[str] = None
    dean_name: Optional[str] = None

class Faculty(FacultyBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True