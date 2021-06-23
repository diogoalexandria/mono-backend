from src.schemas.status_schema import StatusOptions
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field

class CourseBaseSchema(BaseModel):
    name:       str                     = Field(..., example="Math")
    status:     Optional[StatusOptions] = Field( example="active") 

class CourseResponseSchema(CourseBaseSchema):
    id:         UUID                    = Field(..., example="123e4567-e89b-12d3-a456-426614174000")
    name:       str                     = Field(..., example="Math")
    status:     Optional[StatusOptions] = Field(..., example="active")  

class CourseSchema(CourseBaseSchema):
    id:         UUID                    = Field(..., example="123e4567-e89b-12d3-a456-426614174000")      
    created_at: str                     = Field(..., example="2025-12-19 09:26:03.478039")
    updated_at: Optional[str]           = Field(example="2025-12-19 09:26:03.478039")

    class Config:
        orm_mode = True    
    