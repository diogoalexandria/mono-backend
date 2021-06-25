from src.schemas.status_schema import StatusOptions
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field

class ClassBaseSchema(BaseModel):
    name:         str                     = Field(..., example="Math")
    subject_id:   UUID                    = Field(..., example="123e4567-e89b-12d3-a456-426614174000")
    professor_id: Optional[UUID]          = Field(example="123e4567-e89b-12d3-a456-426614174000")  
    status:       Optional[StatusOptions] = Field(example="active") 

class ClassResponseSchema(ClassBaseSchema):
    id:          UUID                     = Field(..., example="123e4567-e89b-12d3-a456-426614174000")
    name:         str                     = Field(..., example="Math")
    subject_id:   UUID                    = Field(..., example="123e4567-e89b-12d3-a456-426614174000")
    professor_id: Optional[UUID]          = Field(example="123e4567-e89b-12d3-a456-426614174000")    
    status:      StatusOptions            = Field(..., example="active")  

class ClassSchema(ClassBaseSchema):
    id:          UUID                    = Field(..., example="123e4567-e89b-12d3-a456-426614174000")      
    created_at:  str                     = Field(..., example="2025-12-19 09:26:03.478039")
    updated_at:  Optional[str]           = Field(example="2025-12-19 09:26:03.478039")

    class Config:
        orm_mode = True