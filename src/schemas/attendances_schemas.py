from src.schemas.status_schema import StatusOptions
from uuid import UUID
from typing import List, Optional
from pydantic import BaseModel, Field

class AttendanceBaseSchema(BaseModel):    
    topic_id:    UUID                      = Field(..., example="123e4567-e89b-12d3-a456-426614174000")
    student_id:  str                       = Field(..., example="123e4567-e89b-12d3-a456-426614174000")

class AttendancesListSchema(BaseModel):
    attendances: List[AttendanceBaseSchema] = Field(..., example=[{
        "topic_id": "123e4567-e89b-12d3-a456-426614174000",
        "student_id": "123e4567-e89b-12d3-a456-426614174000"
     }])   
    
class AttendanceResponseSchema(AttendanceBaseSchema):
    id:          UUID                      = Field(..., example="123e4567-e89b-12d3-a456-426614174000")   
    topic_id:    UUID                      = Field(..., example="123e4567-e89b-12d3-a456-426614174000")    
    student_id:  UUID                      = Field(..., example="123e4567-e89b-12d3-a456-426614174000")    

class AttendanceSchema(AttendanceBaseSchema):
    id:          UUID                      = Field(..., example="123e4567-e89b-12d3-a456-426614174000")      
    created_at:  str                       = Field(..., example="2025-12-19 09:26:03.478039")
    updated_at:  Optional[str]             = Field(example="2025-12-19 09:26:03.478039")

    class Config:
        orm_mode = True