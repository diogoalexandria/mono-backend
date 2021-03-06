from src.schemas.status_schema import StatusOptions
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field

class SubscriptionBaseSchema(BaseModel):    
    class_id:   UUID                     = Field(..., example="123e4567-e89b-12d3-a456-426614174000")
    student_id: Optional[UUID]           = Field(example="123e4567-e89b-12d3-a456-426614174000")    
    status:     Optional[StatusOptions]  = Field(example="active") 

class SubscriptionResponseSchema(SubscriptionBaseSchema):
    id:         UUID                     = Field(..., example="123e4567-e89b-12d3-a456-426614174000")   
    class_id:   UUID                     = Field(..., example="123e4567-e89b-12d3-a456-426614174000")
    student_id: UUID                     = Field(..., example="123e4567-e89b-12d3-a456-426614174000")
    created_at: str                      = Field(..., example="2025-12-19 09:26:03.478039")    
    status:     StatusOptions            = Field(..., example="active")

class SubscriptionUsersResponseSchema(BaseModel):
    id:         UUID                     = Field(..., example="123e4567-e89b-12d3-a456-426614174000")       
    first_name: str                      = Field(..., example="Foo")
    last_name:  str                      = Field(..., example="Bar")      

class SubscriptionSchema(SubscriptionBaseSchema):
    id:          UUID                    = Field(..., example="123e4567-e89b-12d3-a456-426614174000")      
    created_at:  str                     = Field(..., example="2025-12-19 09:26:03.478039")
    updated_at:  Optional[str]           = Field(example="2025-12-19 09:26:03.478039")

    class Config:
        orm_mode = True